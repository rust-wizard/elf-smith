import lief

# Load ELF
elf = lief.parse("test.elf")

# Find .text section
text_section = elf.get_section(".text")
text_bytes = list(text_section.content)

# Original ADD offset
offset_in_text = 0  # first instruction

# Replacement bytes (from step 2)
replacement_bytes = [0x13, 0x03, 0x63, 0x00, 0x13, 0x82, 0x72, 0x00]

# Overwrite original instruction
for i, b in enumerate(replacement_bytes):
    if i + offset_in_text < len(text_bytes):
        text_bytes[i + offset_in_text] = b
    else:
        text_bytes.append(b)  # extend if needed

# Update section content
text_section.content = text_bytes

# Write patched ELF
elf.write("patched.elf")
print("Patched ELF written as patched.elf")
