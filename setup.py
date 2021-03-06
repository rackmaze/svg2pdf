from distutils.core import setup

setup(
    name         = "svg2pdf",
    version      = "0.8.0",
    author       = "Rackmaze",
    author_email = "info@rackmaze.com",
    url          = "https://github.com/kika/svg2pdf",
    packages     = ['svg2pdf'],
    scripts      = ['svg2pdf.py'],
    description  = "SVG2PDF service",
    install_requires = [
          "bottle"
        , "pyaml"
    ]
)
