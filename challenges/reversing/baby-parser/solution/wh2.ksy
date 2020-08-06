meta:
  id: whitehacksv1
  endian: le

seq:
  - id: magic
    contents: ["WHITEHACKSV2", 0x0, 0x0, 0x0, 0x0]
  - id: files
    type: tlv
    repeat: eos

types:
  tlv:
    seq:
      - id: file_name
        type: str
        terminator: 0x0
        encoding: UTF-8
      - id: file_size_compressed
        type: u4
      - id: file_size_uncompressed
        type: u4
      - id: file_data
        size: file_size_compressed
        process: zlib