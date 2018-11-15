# -*- mode: python -*-

block_cipher = None


a = Analysis(['F:\\code\\py_soket-tool\\src\\py_soket-tool.py'],
             pathex=['F:\\code\\py_soket-tool'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='py_soket-tool',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
