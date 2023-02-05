from time import sleep
import os


class Utils:
    def rename_file(self, directory: str, new_file_name: str) -> dict:
        """
        Rename the file with the new name.

        Args:
            diretory: str containing the directory where the file is located.
            new_file_name: str containing the new file name.
        Return:
            dict.
        """
        try:
            for file in os.listdir(directory):
                old_full_path = os.path.join(directory, file)
                new_full_path = os.path.join(directory, new_file_name)
                os.rename(old_full_path, new_full_path)
        except Exception as e:
            return {"error": True, "message": "Error to rename the file", "data": f"{e}"}
        
        return {"error": False, "message": "Rename file successfully", "data": ""}

    def validate_download(self, directory: str) -> dict:
        """
        Validade if download finished.

        Args:
            directory: str containing directory.
        Return:
            dict.
        """
        try:
            while len(os.listdir(directory)) < 1:
                sleep(1)
        except Exception as e:
            return {"error": True, "message": "Download failed.", "data": f"{e}"}
        
        return {"error": False, "message": "Download completed.", "data": ""}
        
    # def send_email(self, sender_email: str, sender_password: str, recipient_email: str, subject: str, text_email: str, attachment: str) -> dict:
    #     """
    #     Send the email to the specified recipient.
        
    #     Args:
    #         sender_email: str containing the sender email.
    #         sender_password: str containing the sender password.
    #         recipient_email: str containing the recipient email
    #         subject: str containing the subject.
    #         text_email: str containing the text email.
    #         attachment: str containing the attachment.
    #     Return:
    #         dict.
    #     """
    #     try:
    #         msg = MIMEMultipart()
    #         msg["From"] =  sender_email
    #         msg["To"] = recipient_email
    #         msg["Subject"] = subject

    #         msg.attach(MIMEText(text_email, "plain"))

    #         part = MIMEBase("application", "octet-stream")
    #         part.set_payload(open(attachment, "rb").read())
    #         encoders.encode_base64(part)
    #         part.add_header("Content-Disposition", "attachment", filename=attachment)
    #         msg.attach(part)

    #         server = smtplib.SMTP("smtp.gmail.com", 587)
    #         server.starttls()
    #         server.login(sender_email, sender_password)
    #         text = msg.as_string()
    #         server.sendmail(sender_email, recipient_email, text)
    #         server.quit()
    #     except Exception as e:
    #         return {"error": True, "message": "Error to send email", "data": f"{e}"}
        
    #     return {"error": False, "message": "Send email successfully", "data": ""}
    