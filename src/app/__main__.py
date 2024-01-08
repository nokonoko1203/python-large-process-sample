import hashlib
import os
import random
import time


def main():
    os.makedirs("output", exist_ok=True)

    for entry in os.scandir("output"):
        if entry.is_file() and entry.path.endswith(".txt"):
            os.remove(entry.path)

    print("Generating large file...")
    generate_large_file("output/large_file.txt", 10_000_000)

    print("Processing cpu bound task...")
    cpu_bound_process()

    print("Processing io bound task...")
    io_bound_process()


def process_line(line):
    return hashlib.md5(line.encode()).hexdigest()


def cpu_bound_process():
    start = time.time()

    with open("output/large_file.txt") as reader, open("output/output_single.txt", "w") as writer:
        for line in reader:
            result = process_line(line.strip())
            writer.write(result + "\n")

    duration = time.time() - start
    print(f"Time taken (Single Thread): {duration} seconds")


def generate_large_file(filename, size):
    with open(filename, "w") as f:
        for _ in range(size):
            f.write(str(random.randint(0, 1000000000)) + "\n")


def generate_files(file_count, lines_per_file):
    for i in range(file_count):
        with open(f"output/file_{i}.txt", "w") as file:
            for _ in range(lines_per_file):
                file.write(str(random.randint(0, 1000000000)) + "\n")


def io_bound_process():
    start = time.time()

    file_count = 10000
    lines_per_file = 10000

    generate_files(file_count, lines_per_file)

    duration = time.time() - start
    print(f"Time taken (Single Thread): {duration} seconds")


if __name__ == "__main__":
    main()
