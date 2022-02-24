#!/usr/bin/env python3
import unittest
from app.models import Review

class ReviewTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Review class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_review = Review(1234,'Python Must Be Crazy',"https://image.tmdb.org/t/p/w500/jdjdjdjn",'So thrilling')
    def tearDown(self):
        Review.clear_reviews()     
    def test_init(self):
        '''
        This will test if the use has been properly initialized
        '''
        self.assertEqual(self.new_review.movie_id,1234)
        self.assertEqual(self.new_review.title,'Python Must Be Crazy')
        self.assertEqual(self.new_review.imageurl,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEqual(self.new_review.review,'So thrilling')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_review, Review))
        
    def test_save_review(self):
        self.new_review.save_review()
        self.assertTrue(len(Review.all_reviews)>0)

    def test_get_reviews(self):
        self.new_review.save_review()
        got_reviews = Review.get_reviews(1234)
        self.assertTrue(len(got_reviews) == 1)
