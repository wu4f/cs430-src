import unittest
import sys
sys.path.insert(0, '../')

from view_header import Route, PresentView, Flash, MSG_TYPE

class TestRoute(unittest.TestCase):

    r1 = Route(True, 'test', {})
    r2 = Route(True, 'test', {0:1, 1:'obj'})

    def test_is_redirect(self):
        self.assertEqual(self.r1.is_redirect(), True)

    def test_get_name(self):
        self.assertEqual(self.r1.get_name(), 'test')

    def test_get_args1(self):
        self.assertEqual(len(self.r1.get_args()), 0)

    def test_get_args2(self):
        self.assertEqual(len(self.r2.get_args()), 2)
        self.assertEqual(self.r2.get_args()[0], 1)
        self.assertEqual(self.r2.get_args()[1], 'obj')

    def test_equals1(self): #basic
        self.assertFalse(self.r1.equals(self.r2))

    def test_equals2(self):
        r2_copy = Route(True, 'test', {0:1, 1:'obj'})
        self.assertTrue(self.r2.equals(r2_copy))

    def test_equals3(self):
        r1_copy = Route(True, 'test', {})
        self.assertTrue(self.r1.equals(r1_copy))

    def test_equals4(self):
        temp = Route(True, 'test_', {})
        self.assertFalse(self.r1.equals(temp))

    def test_equals5(self):
        temp = Route(False, 'test', {})
        self.assertFalse(self.r1.equals(temp))

    def test_equals6(self): #testing the isinstance
        self.assertFalse(self.r1.equals(2))
        self.assertFalse(self.r1.equals('asdf'))
        self.assertFalse(self.r1.equals({}))
        self.assertFalse(self.r1.equals([2]))


class TestPresentView(unittest.TestCase):

    r1 = Route(True, 'test', {})
    r2 = Route(True, 'test', {0:1, 1:'obj'})

    f1 = Flash("test", MSG_TYPE.SUCCESS)
    f2 = Flash("test", MSG_TYPE.FAIL)

    v11 = PresentView(r1, f1)
    v12 = PresentView(r1, f2)
    v21 = PresentView(r2, f1)
    v22 = PresentView(r2, f2)

    def test_get_route1(self): #deep equality
        temp = Route(True, 'test', {})
        self.assertTrue(self.v11.get_route().equals(temp))

    def test_get_route2(self): # pointer equality
        self.assertEqual(self.v11.get_route(), self.r1)

    def test_get_route3(self): # pointer equality
        temp = Route(True, 'test', {})
        self.assertNotEqual(self.v11.get_route(), temp)

    def test_get_flash1(self):
        temp = Flash("test", MSG_TYPE.FAIL)
        self.assertTrue(self.v22.get_flash().equals(temp))

    def test_get_flash2(self): # pointer equality
        self.assertEqual(self.v11.get_flash(), self.f1)

    def test_get_flash3(self): # pointer equality
        temp = Flash("test", MSG_TYPE.SUCCESS)
        self.assertNotEqual(self.v11.get_flash(), temp)
    def test_get_flash4(self): # pointer equality
        temp = PresentView(self.r2)
        self.assertEqual(temp.get_flash(), None)
    #
    def test_equals1(self):
        self.assertFalse(self.v11.equals(self.v12))

    def test_equals2(self):
        self.assertFalse(self.v11.equals(2))

    def test_equals3(self):
        self.assertTrue(self.v11.equals(self.v11))

    def test_equals4(self):
        temp = PresentView(self.r2, self.f1)
        self.assertTrue(self.v21.equals(temp))

    def test_equals5(self):
        temp = Flash("FAILLL", MSG_TYPE.SUCCESS)
        temp = PresentView(self.r2, temp)
        self.assertFalse(self.v21.equals(temp))

    def test_equals6(self): # None flash
        temp = PresentView(self.r2)
        self.assertFalse(temp.equals(self.v11))

    def test_equals7(self): # None flash
        temp = PresentView(self.r2)
        self.assertFalse(self.v22.equals(temp))

    def test_equals8(self): # None flash
        temp = PresentView(self.r2)
        temp2 = PresentView(self.r2)
        self.assertFalse(temp.equals(temp2))

    def test_equals9(self): # None flash
        temp = PresentView(self.r2)
        self.assertFalse(temp.equals(temp))

class TestFlash(unittest.TestCase):

    f1 = Flash("test", MSG_TYPE.SUCCESS)
    f2 = Flash("test", MSG_TYPE.FAIL)
    f3 = Flash(1, MSG_TYPE.FAIL)

    def test_equals1(self):
        f1_copy = Flash("test", MSG_TYPE.SUCCESS)
        self.assertTrue(self.f1.equals(f1_copy))

    def test_equals2(self):
        f1_copy = Flash("test 2", MSG_TYPE.SUCCESS)
        self.assertFalse(self.f1.equals(f1_copy))

    def test_equals3(self): #testing the isinstance
        self.assertFalse(self.f1.equals(2))
        self.assertFalse(self.f1.equals('asdf'))
        self.assertFalse(self.f1.equals({}))
        self.assertFalse(self.f1.equals([2]))

    def test_equals4(self):
        self.assertFalse(self.f1.equals(self.f2))

    def test_gm1(self):
        self.assertEqual(self.f1.get_msg(), 'test')

    def test_gmt2(self):
        self.assertEqual(self.f1.get_msg_type(), MSG_TYPE.SUCCESS)

    def test_gmt3(self):
        self.assertEqual(self.f2.get_msg_type(), MSG_TYPE.FAIL)

class Test_MSG_TYPE(unittest.TestCase):
    s = MSG_TYPE.SUCCESS
    f = MSG_TYPE.FAIL

    def test_success(self):
        self.assertEqual(self.s.value, 'success')
        self.assertEqual(self.s.name, 'SUCCESS')

    def test_fail(self):
        self.assertEqual(self.f.value, 'danger')
        self.assertEqual(self.f.name, 'FAIL')

    # FAIL = 'danger'
if __name__ == '__main__':
    unittest.main()
