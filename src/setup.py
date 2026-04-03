from setuptools import setup
import setup_translate

pkg = 'Extensions.Sudoku'
setup(name='enigma2-plugin-extensions-sudoku',
       version='3.0',
       description='Sudoku Game FHD modded by Lululla',
       package_dir={pkg: 'Sudoku'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'Readme.txt', 'sudoku.png', 'pic/*.png', 'pic/*.jpg']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
