from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from course import CourseClass
from student import studentClass


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Result Management System")
        self.root.geometry("1500x700+0+0")
        self.root.config(bg="white")

        # icon
        self.logo_dash = ImageTk.PhotoImage(file="images/Python.png")

        # title
        title = Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, font=(
            "tahoma", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        # Menu
        M_frame = LabelFrame(self.root, text="Home", font=(
            "times new roman", 15), bg="white")
        M_frame.place(x=10, y=70, width=300, height=450)

        btn_course = Button(M_frame, text="Add New Students", font=("tahoma", 15, "bold"), bg="#0b5377",
                            fg="white", cursor="hand2", command=self.add_course).place(x=40, y=5, width=200, height=50)
        btn_student = Button(M_frame, text="Students List", font=("tahoma", 15, "bold"),
                             bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=40, y=75, width=200, height=50)
        btn_result = Button(M_frame, text="Add New Courses", font=("tahoma", 15, "bold"), bg="#0b5377",
                            fg="white", cursor="hand2").place(x=40, y=145, width=200, height=50)
        btn_view = Button(M_frame, text="Courses List", font=("tahoma", 15, "bold"),
                          bg="#0b5377", fg="white", cursor="hand2").place(x=40, y=215, width=200, height=50)
        btn_logout = Button(M_frame, text="Add New Results", font=("tahoma", 15, "bold"), bg="#0b5377",
                            fg="white", cursor="hand2").place(x=40, y=285, width=200, height=50)
        btn_exit = Button(M_frame, text="Results List", font=("tahoma", 15, "bold"), bg="#0b5377",
                          fg="white", cursor="hand2").place(x=40, y=355, width=200, height=50)

        # content_window
        self.bg_img = Image.open("Images/Profile_Background.jpg")
        self.bg_img = self.bg_img.resize((920, 350), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img).place(
            x=500, y=200, width=920, height=350)

        # update_details
        '''self.lbl_course = Label(self.root, text="Total Courses\n[0]", font=(
            "tahoma", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=500, y=565, width=300, height=80)

        self.lbl_student = Label(self.root, text="Total Courses\n[0]", font=(
            "tahoma", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=710, y=565, width=300, height=80)

        self.lbl_result = Label(self.root, text="Total Results\n[0]", font=(
            "tahoma", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=565, width=300, height=80)'''

        # footer
        footer = Label(self.root, text="SRMS\nContact Us for any Technical Issue: 6493219160", font=(
            "tahoma", 12, "bold"), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)

    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
