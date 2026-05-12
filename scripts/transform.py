import lief

elf = lief.parse("test.elf")

# 1. Create new patch section
patch_section = lief.ELF.Section(".patch")
patch_section.content = [
    0x13, 0x45, 0x03, 0x00,  # XORI x10,x6,0
    0x93, 0xc5, 0x03, 0x00,  # XORI x11,x7,0
    0xb3, 0x02, 0xb5, 0x00   # ADD x5,x10,x11
]
patch_section.type  = 1        # SHT_PROGBITS
patch_section.flags = 0x2 | 0x4  # ALLOC | EXECINSTR
elf.add(patch_section, loaded=True)

# 2. Replace first instruction in .text with NOP safely
text_section = elf.get_section(".text")
text_bytes = list(text_section.content)
text_bytes[0:4] = [0x13, 0x00, 0x00, 0x00]  # NOP
text_section.content = text_bytes

# 3. Write patched ELF
elf.write("patched.elf")
print("Patched ELF successfully written")