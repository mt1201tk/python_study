test_set_1 = set()
 
test_set_1.add('python')
test_set_1.update({'-', 'izm', '.', 'com'})
 
print(test_set_1)

#�P��̗v�f��ǉ�����ꍇ��add�A���̃Z�b�g�⃊�X�g�A�^�v���Ȃǂ���v�f��ǉ�����ꍇ��update���g�p���܂��B





test_set_1 = {'python', '-', 'izm', '.', 'com'}
 
test_set_1.remove('-')
test_set_1.discard('.')
 
print(test_set_1)

#�Z�b�g����v�f���폜����ꍇ��remove�Adiscard���g�p���܂��B





test_set_1 = frozenset({'python', '-', 'izm', '.', 'com'})
 
# test_set_1.remove('-')
# test_set_1.discard('.')
 
print(test_set_1)

#frozenset��frozenset�֐����g�p���Ēʏ��set�̂悤�ɍ쐬�ł��܂��B
