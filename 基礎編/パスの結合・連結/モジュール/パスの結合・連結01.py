import os


PROJECT_DIR = 'C:?python-izm'
SETTINGS_FILE = 'settings.ini'

print(os.path.join(PROJECT_DIR, SETTINGS_FILE))
print(os.path.join(PROJECT_DIR, 'settings_dir', SETTINGS_FILE))

#Python�ł̓p�X�̌�����A�����s���֐����p�ӂ���Ă��܂��B
#�p�X�������E�A������ɂ�os.path.join���g�p���܂��B

