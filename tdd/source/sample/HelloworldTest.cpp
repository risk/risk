// -*- coding:utf-8 -*-

#include <gtest/gtest.h>

class Helloworld : public ::testing::Test
{
};

TEST_F(Helloworld, initialize)
{
	EXPECT_EQ(0, 1);
}


