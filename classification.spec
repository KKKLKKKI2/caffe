# -*- mode: python -*-

block_cipher = None


a = Analysis(['classification.py'],
             pathex=['C:\\Users\\D300_ADAS\\Desktop\\caffe-windows\\python'],
             binaries=[],
             datas=[skimage.io._plugins],
             hiddenimports=[skimage.io._plugins],
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
          exclude_binaries=True,
          name='classification',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='classification')
