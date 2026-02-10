#!/usr/bin/env python3
import re
import sys
from pathlib import Path

def extract_grpc_methods(file_path):
    """Extract method names from _grpc.py file"""
    methods = []
    try:
        content = Path(file_path).read_text()
        pattern = r'@abc.abstractmethod\s+async def (\w+)\(self, stream:'
        methods = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
        if not methods:
            # Try simpler pattern for ServiceBase
            lines = content.split('\n')
            in_service_base = False
            for i, line in enumerate(lines):
                if 'class ' in line and 'ServiceBase' in line and 'abc.ABC' in line:
                    in_service_base = True
                elif in_service_base and line.strip().startswith('class '):
                    in_service_base = False
                elif in_service_base and 'async def ' in line:
                    match = re.search(r'async def (\w+)\(', line)
                    if match and not match.group(1).startswith('_'):
                        methods.append(match.group(1))
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    return set(methods)

def extract_abstract_methods(file_path):
    """Extract abstract method names from base class"""
    methods = []
    try:
        content = Path(file_path).read_text()
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '@abc.abstractmethod' in line or '@abstractmethod' in line:
                for j in range(i+1, min(i+5, len(lines))):
                    match = re.match(r'\s*async def (\w+)\(', lines[j])
                    if match:
                        methods.append(match.group(1))
                        break
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    return set(methods)

def extract_client_methods(file_path):
    """Extract implemented methods from client class"""
    methods = []
    try:
        content = Path(file_path).read_text()
        # Look for async def methods but exclude private/special methods
        pattern = r'\n    async def (\w+)\('
        methods = re.findall(pattern, content)
        methods = [m for m in methods if not m.startswith('_')]
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    return set(methods)

def extract_service_handlers(file_path):
    """Extract RPC handler methods from service class"""
    methods = []
    try:
        content = Path(file_path).read_text()
        # Find methods that are RPC handlers (usually PascalCase) in the RPC service class
        lines = content.split('\n')
        in_rpc_class = False
        for i, line in enumerate(lines):
            if 'class ' in line and 'RPCService' in line or 'class ' in line and 'Service(' in line:
                in_rpc_class = True
            elif in_rpc_class and line.strip().startswith('class ') and 'RPCService' not in line:
                in_rpc_class = False
            elif in_rpc_class and 'async def ' in line:
                match = re.search(r'async def ([A-Z]\w+)\(', line)
                if match:
                    methods.append(match.group(1))
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
    return set(methods)

def pascal_to_snake(pascal_str):
    """Convert PascalCase to snake_case"""
    # Handle special cases
    special_cases = {
        'Get3DModels': 'get_3d_models',
        'ListUUIDs': 'list_uuids',
        'GetGPIO': 'get_gpio',
        'SetGPIO': 'set_gpio',
        'PWM': 'pwm',
        'SetPWM': 'set_pwm',
        'PWMFrequency': 'pwm_frequency',
        'SetPWMFrequency': 'set_pwm_frequency',
    }
    if pascal_str in special_cases:
        return special_cases[pascal_str]
    result = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', pascal_str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', result).lower()

if __name__ == '__main__':
    grpc_file = sys.argv[1] if len(sys.argv) > 1 else None
    base_file = sys.argv[2] if len(sys.argv) > 2 else None
    client_file = sys.argv[3] if len(sys.argv) > 3 else None
    service_file = sys.argv[4] if len(sys.argv) > 4 else None
    
    grpc_methods = extract_grpc_methods(grpc_file) if grpc_file else set()
    base_methods = extract_abstract_methods(base_file) if base_file else set()
    client_methods = extract_client_methods(client_file) if client_file else set()
    service_methods = extract_service_handlers(service_file) if service_file else set()
    
    # Common methods that are inherited from ComponentBase/ServiceBase
    common_methods = {'DoCommand', 'GetGeometries', 'GetKinematics', 'Get3DModels'}
    
    print(f"PROTOBUF: {sorted(grpc_methods)}")
    print(f"BASE: {sorted(base_methods)}")
    print(f"CLIENT: {sorted(client_methods)}")
    print(f"SERVICE: {sorted(service_methods)}")
    
    # Find missing methods
    missing_base = []
    for method in sorted(grpc_methods):
        snake_method = pascal_to_snake(method)
        if snake_method not in base_methods and method not in common_methods:
            missing_base.append(f"  {method} ({snake_method})")
    
    missing_client = []
    for method in sorted(grpc_methods):
        snake_method = pascal_to_snake(method)
        if snake_method not in client_methods:
            missing_client.append(f"  {method} ({snake_method})")
    
    missing_service = []
    for method in sorted(grpc_methods):
        if method not in service_methods:
            missing_service.append(f"  {method}")
    
    if missing_base:
        print("\n=== MISSING IN BASE ===")
        for m in missing_base:
            print(m)
    
    if missing_client:
        print("\n=== MISSING IN CLIENT ===")
        for m in missing_client:
            print(m)
    
    if missing_service:
        print("\n=== MISSING IN SERVICE ===")
        for m in missing_service:
            print(m)
    
    if not (missing_base or missing_client or missing_service):
        print("\n✓ ALL METHODS IMPLEMENTED")
