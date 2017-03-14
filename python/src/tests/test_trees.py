# pylint: disable=W0621
# pylint: disable=W0212
# pylint: disable=C0103

import pytest

from pkg.red_black_tree import _NilNode
from pkg.avl_tree import AVLTree
_TREE_TYPE = AVLTree

_DEFAULT_KEY = 42
_DEFAULT_KEY_2 = _DEFAULT_KEY * 2
_DEFAULT_KEY_3 = _DEFAULT_KEY_2 * 2
_DEFAULT_KEY_4 = _DEFAULT_KEY_3 * 2
# _DEFAULT_VALUE = 4.2


@pytest.fixture
def zero_element_tree():
    return _TREE_TYPE()


@pytest.fixture
def one_element_tree(zero_element_tree):
    zero_element_tree.insert(_DEFAULT_KEY)
    return zero_element_tree


@pytest.fixture
def two_element_tree(one_element_tree):
    one_element_tree.insert(_DEFAULT_KEY_2)
    return one_element_tree


@pytest.fixture
def three_element_tree(two_element_tree):
    two_element_tree.insert(_DEFAULT_KEY_3)
    return two_element_tree


@pytest.fixture
def wikipedia_example_avl_tree_balanced(zero_element_tree):
    tree = zero_element_tree
    for node in ['j', 'f', 'p', 'd', 'g', 'l', 'v', 'c', 'n', 's', 'x', 'q', 'u']:
        tree.insert(node)
    return tree


# todo: this should be less lenient for RedBlackTree
def assert_not_node(node):
    assert node is None or isinstance(node, _NilNode)


def test_zero_element_tree(zero_element_tree):
    assert_not_node(zero_element_tree._root)


def test_one_element_tree(one_element_tree):
    assert one_element_tree._root._key == _DEFAULT_KEY
    assert_not_node(one_element_tree._root._left)
    assert_not_node(one_element_tree._root._right)


def test_two_element_tree(two_element_tree):
    assert two_element_tree._root._key == _DEFAULT_KEY
    assert_not_node(two_element_tree._root._left)
    assert two_element_tree._root._right._key == _DEFAULT_KEY_2
    assert_not_node(two_element_tree._root._right._left)
    assert_not_node(two_element_tree._root._right._right)


def test_three_element_tree(three_element_tree):
    assert three_element_tree._root._key == _DEFAULT_KEY
    assert_not_node(three_element_tree._root._left)
    assert three_element_tree._root._right._key == _DEFAULT_KEY_2
    assert_not_node(three_element_tree._root._right._left)
    assert three_element_tree._root._right._right._key == _DEFAULT_KEY_3
    assert_not_node(three_element_tree._root._right._right._left)
    assert_not_node(three_element_tree._root._right._right._right)


def test_zero_element_tree_find_failure(zero_element_tree):
    assert _DEFAULT_KEY not in zero_element_tree


def test_one_element_tree_find_success(one_element_tree):
    assert _DEFAULT_KEY in one_element_tree


def test_one_element_tree_find_failure(one_element_tree):
    assert _DEFAULT_KEY_2 not in one_element_tree


def test_two_element_tree_find_success(two_element_tree):
    assert _DEFAULT_KEY in two_element_tree
    assert _DEFAULT_KEY_2 in two_element_tree


def test_two_element_tree_find_failure(two_element_tree):
    assert _DEFAULT_KEY_3 not in two_element_tree


def test_three_element_tree_find_success(three_element_tree):
    assert _DEFAULT_KEY in three_element_tree
    assert _DEFAULT_KEY_2 in three_element_tree
    assert _DEFAULT_KEY_3 in three_element_tree


def test_three_element_tree_find_failure(three_element_tree):
    assert _DEFAULT_KEY_4 not in three_element_tree


def test_wikipedia_example_avl_tree_balanced_is_balanced(wikipedia_example_avl_tree_balanced):
    tree = wikipedia_example_avl_tree_balanced

    assert tree._root._key == 'j'
    assert tree._root._left._key == 'f'
    assert tree._root._right._key == 'p'
    assert tree._root._left._left._key == 'd'
    assert tree._root._left._right._key == 'g'
    assert tree._root._right._left._key == 'l'
    assert tree._root._right._right._key == 'v'
    assert tree._root._left._left._left._key == 'c'
    assert tree._root._right._left._right._key == 'n'
    assert tree._root._right._right._left._key == 's'
    assert tree._root._right._right._right._key == 'x'
    assert tree._root._right._right._left._left._key == 'q'
    assert tree._root._right._right._left._right._key == 'u'


def test_wikipedia_example_avl_tree_balanced_heights(wikipedia_example_avl_tree_balanced):
    tree = wikipedia_example_avl_tree_balanced

    assert tree._root._calculate_height() == 5
    assert tree._root._left._calculate_height() == 3
    assert tree._root._right._calculate_height() == 4
    assert tree._root._left._left._calculate_height() == 2
    assert tree._root._left._right._calculate_height() == 1
    assert tree._root._right._left._calculate_height() == 2
    assert tree._root._right._right._calculate_height() == 3
    assert tree._root._left._left._left._calculate_height() == 1
    assert tree._root._right._left._right._calculate_height() == 1
    assert tree._root._right._right._left._calculate_height() == 2
    assert tree._root._right._right._right._calculate_height() == 1
    assert tree._root._right._right._left._left._calculate_height() == 1
    assert tree._root._right._right._left._right._calculate_height() == 1


def test_wikipedia_example_avl_tree_balanced_balance_factors(wikipedia_example_avl_tree_balanced):
    tree = wikipedia_example_avl_tree_balanced

    assert tree._root._calculate_balance_factor() == 1
    assert tree._root._left._calculate_balance_factor() == -1
    assert tree._root._right._calculate_balance_factor() == 1
    assert tree._root._left._left._calculate_balance_factor() == -1
    assert tree._root._left._right._calculate_balance_factor() == 0
    assert tree._root._right._left._calculate_balance_factor() == 1
    assert tree._root._right._right._calculate_balance_factor() == -1
    assert tree._root._left._left._left._calculate_balance_factor() == 0
    assert tree._root._right._left._right._calculate_balance_factor() == 0
    assert tree._root._right._right._left._calculate_balance_factor() == 0
    assert tree._root._right._right._right._calculate_balance_factor() == 0
    assert tree._root._right._right._left._left._calculate_balance_factor() == 0
    assert tree._root._right._right._left._right._calculate_balance_factor() == 0


if __name__ == '__main__':
    pytest.main()