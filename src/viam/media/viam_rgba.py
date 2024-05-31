# Viam uses a special header prepended to raw RGBA data. The header is composed of a
# 4-byte magic number followed by a 4-byte line of the width as a uint32 number
# and another for the height. Credit to Ben Zotto for inventing this formulation
# https://bzotto.medium.com/introducing-the-rgba-bitmap-file-format-4a8a94329e2c

RGBA_MAGIC_NUMBER = bytes("RGBA", "utf-8")

RGBA_FORMAT_LABEL = "VIAM_RGBA"

RGBA_HEADER_LENGTH = 12
