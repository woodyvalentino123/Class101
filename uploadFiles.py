import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
       #upload a file to Dropbox using API v2
        
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A6uPTyN35YotAaQwp9aHjiDgvDisZjFp7pnKSGoE05qx3l5v_wHcc5i7nz64sNxlBS2Pnji_Q3rZuIKFv6Tpos4t8EUHpdHKHugLu74-Jf2_z2xSAf4MqynJ92Lnt6VuGlBc4As'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full file path to upload to dropbox: ") 

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved")

main()