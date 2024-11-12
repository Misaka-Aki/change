from docx import Document

def replace_punctuation(file_path):
    # 定义英文标点与中文标点的对应关系
    replacements = {
        ",": "，",
        ".": "。",
        ":": "：",
        ";": "；",
        "?": "？",
        "!": "！",
        "'": "‘",
        "(": "（",
        ")": "）"
    }

    # 打开Word文档
    doc = Document(file_path)

    # 遍历文档中的所有段落并替换
    for para in doc.paragraphs:
        for en_punc, zh_punc in replacements.items():
            para.text = para.text.replace(en_punc, zh_punc)

    # 保存修改后的文档
    output_path = "modified_" + file_path.split("/")[-1]
    doc.save(output_path)
    print(f"替换完成，已保存为 {output_path}")

# 通过用户输入获取文件路径
file_path = input("请输入Word文档的路径：")
replace_punctuation(file_path)
