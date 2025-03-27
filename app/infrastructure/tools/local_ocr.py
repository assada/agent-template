from app.domain.interfaces.tool_interface import ToolInterface
import io
import fitz  # PyMuPDF
from app.utils.logger import Logger


class LocalOCRTool(ToolInterface):
    def __init__(self):
        super().__init__("Local OCR", "Extract text from an image using local OCR")
        self.logger = Logger("Local OCR Tool")

    def execute(self, input: any) -> str:
        self.logger.debug("Executing Local OCR Tool")
        self.logger.debug(input)

        pdf_bytes = input.get("file_content")
        pdf_stream = io.BytesIO(pdf_bytes)
        
        pdf_document = fitz.open(stream=pdf_stream, filetype="pdf")
        
        text_content = ""
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text_content += page.get_text()
        
        pdf_document.close()
        
        self.logger.debug(f"Extracted text: {text_content[:100]}...")

        return text_content