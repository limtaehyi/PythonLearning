from pathlib import Path

#임포트 및 경로 생성
path = Path("path/to/some/directory")

#새로운 디렉토리 생성
path.mkdir(parents=True, exist_ok=True)

#경로에서 파일 및 폴더 생성
for file in path.glob("*"):
    print(file)

#파일 정보 확인
for file in path.glob("*"):
    print(file)
    print("Is file:", file.is_file())
    print("Is directory:", file.is_dir())
    print("File size:", file.stat().st_size, "bytes")

#파일 내용 읽기
file_path = Path("path/to/some/file.txt")

with file_path.open("r") as f:
    content =.read()
    print(content)

#파일 작성
file_path = Path("path/to/some/new_file.txt")

with file_path.open("w") as f:
    f.write("Hello, pathlib!")

#파일 이름, 확장자 및 부모 디렉토리 얻기
file_path = Path("path/to/some/file.txt")

print("File name:", file_path.name)
printFile stem:", file_path.stem)
print("File suffix:", file_path.suffix)
print("Parent directory:", file_path.parent)

#파일 경로 조작
file_path = Path("/to/some/file.txt")

new_path = file_path.with_name("new_file.txt")
print("New path:", new_path)

path_without_ext = file_path.with_suffix("")
print("Path without extension:", path_without_ext)

path_with_new_ext = file_path.with_suffix(".log")
print("Path with new extension:", path_with_new_ext)

#상대 경로 생성 및 해석
base_path = Path("base/directory")
relative_path = Path("some/other/directory")

abs_path = base_path / relative_path
print("Absolute path:", abs_path)

resolved_path = abs_path.resolve()
print("Resolved path:", resolved_path)
