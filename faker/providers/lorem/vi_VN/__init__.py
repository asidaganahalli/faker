from typing import Dict

from .. import Provider as LoremProvider


class Provider(LoremProvider):
    """Implement lorem provider for ``vi_VN`` locale.

    Word list is based on common Vietnamese words and phrases.
    """

    word_list = (
        "cái",
        "đó",
        "là",
        "và",
        "có",
        "như",
        "một",
        "để",
        "cũng",
        "với",
        "cho",
        "trong",
        "tôi",
        "của",
        "người",
        "không",
        "sẽ",
        "đã",
        "này",
        "theo",
        "làm",
        "nơi",
        "đang",
        "nếu",
        "bạn",
        "được",
        "khi",
        "thì",
        "về",
        "mà",
        "cũng",
        "nào",
        "của",
        "nhưng",
        "vì",
        "rất",
        "tại",
        "tại",
        "thế",
        "để",
        "giữa",
        "với",
        "cách",
        "từ",
        "lớn",
        "có",
        "vài",
        "hơn",
        "vẫn",
        "dưới",
        "đi",
        "đến",
        "vậy",
        "điều",
        "hoặc",
        "chỉ",
        "hơn",
        "khiến",
        "giống",
        "sau",
        "trong",
        "đúng",
        "của",
        "mỗi",
        "như",
        "bên",
        "để",
        "chưa",
        "như",
        "thay",
        "như",
        "các",
        "tự",
        "số",
        "từng",
        "nhiều",
        "gần",
        "từ",
    )

    parts_of_speech: Dict[str, tuple] = {
        "verb": (
            "là",
            "có",
            "làm",
            "đi",
            "nói",
            "thấy",
            "nghe",
            "đọc",
            "viết",
            "muốn",
            "đi",
            "ngồi",
            "uống",
            "ăn",
            "học",
            "chơi",
            "nhìn",
            "được",
            "tìm",
            "đặt",
            "giúp",
            "hỏi",
            "giải",
            "mua",
            "bán",
            "nói",
        ),
        "noun": (
            "người",
            "sách",
            "máy",
            "bàn",
            "ghế",
            "cửa",
            "nhà",
            "bút",
            "xe",
            "điện thoại",
            "bánh",
            "cà phê",
            "nước",
            "trường",
            "chúng tôi",
            "học sinh",
            "giáo viên",
            "bố",
            "mẹ",
            "em",
            "anh",
            "chị",
        ),
        "adverb": (
            "thực sự",
            "rất",
            "nhanh",
            "chậm",
            "tốt",
            "xấu",
            "đúng",
            "sai",
            "vui",
            "buồn",
            "mới",
            "cũ",
            "dễ",
            "khó",
            "gần",
            "xa",
            "hơn",
            "vẫn",
            "đã",
            "mới",
        ),
        "adjective": (
            "đẹp",
            "xấu",
            "tốt",
            "xấu",
            "to",
            "nhỏ",
            "ngọt",
            "chua",
            "mặn",
            "nhanh",
            "chậm",
            "đầu",
            "cuối",
            "mới",
            "cũ",
            "dễ",
            "khó",
            "hơi",
            "vui",
            "buồn",
            "mạnh",
            "yếu",
        ),
    }
