from fontTools.ttLib import TTFont

from fontbakery.checkrunner import FAIL
from fontbakery.codetesting import (assert_PASS,
                                    assert_results_contain,
                                    CheckTester,
                                    TEST_FILE)
from fontbakery.profiles import layout as layout_profile


def test_check_layout_valid_feature_tags():
    """Does the font have any invalid feature tags?"""
    check = CheckTester(layout_profile,
                        "com.google.fonts/check/layout_valid_feature_tags")

    ttFont = TTFont(TEST_FILE("nunito/Nunito-Regular.ttf"))
    assert_PASS(check(ttFont))


    ttFont = TTFont(TEST_FILE("rosarivo/Rosarivo-Regular.ttf"))
    assert_results_contain(check(ttFont),
                           FAIL, 'bad-feature-tags')


def test_check_layout_valid_script_tags():
    """Does the font have any invalid script tags?"""
    check = CheckTester(layout_profile,
                        "com.google.fonts/check/layout_valid_script_tags")

    ttFont = TTFont(TEST_FILE("nunito/Nunito-Regular.ttf"))
    assert_PASS(check(ttFont))


    ttFont = TTFont(TEST_FILE("rosarivo/Rosarivo-Regular.ttf"))
    assert_results_contain(check(ttFont),
                           FAIL, 'bad-script-tags')


def test_check_layout_valid_language_tags():
    """Does the font have any invalid language tags?"""
    check = CheckTester(layout_profile,
                        "com.google.fonts/check/layout_valid_language_tags")

    ttFont = TTFont(TEST_FILE("nunito/Nunito-Regular.ttf"))
    assert_PASS(check(ttFont))


    ttFont = TTFont(TEST_FILE("rosarivo/Rosarivo-Regular.ttf"))
    assert_results_contain(check(ttFont),
                           FAIL, 'bad-language-tags')
