class TextProcessor:
    @staticmethod
    def remove_punctuation(text: str) -> str:
        """去除句尾标点符号"""
        return text.rstrip(',.。，!！?？')

    @staticmethod
    def format_subtitle_block(index: int, start_time: str, end_time: str, text: str) -> list:
        """格式化单个字幕块"""
        return [
            str(index),
            f"{start_time} --> {end_time}",
            text,
            ""
        ]

    @staticmethod
    def format_speaker_text(speaker: str, text: str) -> str:
        """格式化带说话人的文本"""
        return f"{speaker} {text}" if speaker else text
