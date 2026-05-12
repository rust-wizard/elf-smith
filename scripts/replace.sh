riscv32-unknown-elf-as -march=rv32i -o diff.o diff.s
riscv32-unknown-elf-objcopy -O binary diff.o diff.bin
xxd diff.bin
