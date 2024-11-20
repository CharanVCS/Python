from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", ln=True, align="C")

    def add_shirtificate(self, name, shirt_path):
        self.add_page()

        # Set the title
        self.set_font("Arial", "B", 24)
        self.cell(0, 60, "", ln=True)  # Add some space from the top

        # Add the shirt image
        self.image(shirt_path, x=(210 - 150) / 2, y=80, w=150)

        # Add the user's name
        self.set_font("Arial", "B", 24)
        self.set_text_color(255, 255, 255)
        self.cell(0, 190, name, ln=True, align="C")

def main():
    name = input("Enter your name: ")
    shirt_path = "shirtificate.png"  # Ensure the shirt image file is available at this path

    pdf = PDF(orientation='P', format='A4')
    pdf.add_shirtificate(name, shirt_path)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
