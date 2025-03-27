from mistralai import DocumentURLChunk, Mistral
from app.config import Config
from app.domain.interfaces.tool_interface import ToolInterface
from app.utils.logger import Logger


class MistralOCRTool(ToolInterface):
    def __init__(self):
        super().__init__("Mistral OCR", "Extract text from an image using Mistral AI")
        self.mistralClient = Mistral(api_key=Config.MISTRAL_API_KEY)
        self.logger = Logger("Mistral OCR Tool")

    def execute(self, input: any) -> str:
        self.logger.debug("Executing OCR Tool")
        self.logger.debug(input)
        uploaded_file = self.mistralClient.files.upload(
            file={
                "file_name": input.get("file_name"),
                "content": input.get("file_content"),
            },
            purpose="ocr",
        )
        signed_url = self.mistralClient.files.get_signed_url(file_id=uploaded_file.id, expiry=1)
        self.logger.debug(f"Signed URL: {signed_url.url}")
        pdf_response = self.mistralClient.ocr.process(
            document=DocumentURLChunk(document_url=signed_url.url),
            model="mistral-ocr-latest",
            include_image_base64=False
        )
        self.logger.debug("PDF Response:")
        self.logger.debug(pdf_response)
        self.logger.debug(pdf_response.model_dump())

        all_pages = "\n".join([page.markdown for page in pdf_response.pages])
        self.logger.debug(f"All Pages: {all_pages}")


        return all_pages ## todo: add error handling
