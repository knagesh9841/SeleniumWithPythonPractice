import autoit


def uploadfile(filename):
    autoit.win_wait("File Upload", 4)
    autoit.control_focus("File Upload", "Edit1")
    autoit.control_set_text("File Upload", "Edit1", filename)
    autoit.control_click("File Upload", "Button1")

