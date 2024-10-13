import os


class FileUtil:
    """
    ファイル操作を行うユーティリティクラス。
    """

    @staticmethod
    def read_file(file_path: str) -> str:
        """
        指定されたファイルを読み込み、内容を返す。

        Args:
            file_path: ファイルパス

        Returns:
            ファイルの内容
        """
        file_path = os.path.join(os.path.dirname(__file__), file_path)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return content

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        """
        指定されたファイルに内容を書き込む。

        Args:
            file_path: ファイルパス
            content: ファイルに書き込む内容
        """
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
