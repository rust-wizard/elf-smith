riscv32-unknown-elf-as -march=rv32i -o test.o test.s
riscv32-unknown-elf-ld -Ttext=0x0 -o test.elf test.o
riscv32-unknown-elf-objdump -d test.elf
