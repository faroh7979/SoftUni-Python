from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero('Klopp', 99, 1000, 500)
        self.enemy_hero = Hero('Guardiola', 89, 900, 450)

    def test_correct_initialisation(self):
        self.assertEqual('Klopp', self.hero.username)
        self.assertEqual(99, self.hero.level)
        self.assertEqual(1000, self.hero.health)
        self.assertEqual(500, self.hero.damage)

    def test_equal_usernames_should_raises_exception(self):

        self.enemy_hero.username = 'Klopp'
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_my_hero_health_is_zero_or_less_should_raise_value_error(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_hero_health_is_zero_or_less_should_raise_value_error(self):
        self.enemy_hero.health = - 1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ve.exception))

    def test_decreasing_of_my_hero_health(self):
        enemy_hero_damage = self.enemy_hero.damage * self.enemy_hero.level
        my_expected_current_blood = self.hero.health - enemy_hero_damage
        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.hero.health, my_expected_current_blood)

    def test_decreasing_of_enemy_health(self):
        my_hero_damage = self.hero.damage * self.hero.level
        enemy_expected_current_blood = self.enemy_hero.health - my_hero_damage

        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.enemy_hero.health, enemy_expected_current_blood)

    def test_draw(self):
        self.hero.health = 1
        self.enemy_hero.health = 1

        state = self.hero.battle(self.enemy_hero)
        self.assertEqual("Draw", state)

    def test_my_win(self):
        self.enemy_hero.health = 1
        self.enemy_hero.damage = 0
        state = self.hero.battle(self.enemy_hero)

        self.assertEqual(self.hero.level, 100)
        self.assertEqual(self.hero.health, 1005)
        self.assertEqual(self.hero.damage, 505)
        self.assertEqual(state, "You win")

    def test_my_lose(self):
        self.hero.health = 1
        self.hero.damage = 0
        state = self.hero.battle(self.enemy_hero)

        self.assertEqual(self.enemy_hero.level, 90)
        self.assertEqual(self.enemy_hero.health, 905)
        self.assertEqual(self.enemy_hero.damage, 455)
        self.assertEqual(state, "You lose")

    def test__str__method(self):
        expected_result = "Hero Klopp: 99 lvl\nHealth: 1000\nDamage: 500\n"
        self.assertEqual(expected_result, str(self.hero))


if __name__ == '__main__':
    main()