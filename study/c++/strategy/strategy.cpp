#include <iostream>

class Foods
{
private:

	int amount_;
	int quality_;

public:

	Foods(int amount, int quality)
		: amount_(amount)
		, quality_(quality)
	{
	}

	virtual getAmount() const
	{
		return amount_;
	}

	virtual getQuality()
	{
		return quality_;
	}
};


class FoodsComparator
{
public:

    int compare(const Foods& lhs, const Foods& rhs) = 0;
};

class KouchanComparator
	: public FoodsComparator
{
public:

    int compare(const Foods& lhs, const Foods& rhs)
	{
    int compare(const Foods& lhs, const Foods& rhs)
	{
		// こうちゃんは、味8割 量2割
		int lhsValue = lhs.getAmount() / 100 * 0.8 + lhs.getAmount() * ;
		int rhsValue = rhs.getAmount();
		return
			(lhsValue == rhsValue) ? 0 :
			(lhsValue > rhsValue) ? -1 :
			1;
	}
	}
};


class LenokunComparator
	: public FoodsComparator
{
public:

    int compare(const Foods& lhs, const Foods& rhs)
	{
		// レノくんは、味2割 量8割
		int lhsAmount = lhs.getAmount();
		int rhsAmount = lhs.getAmount();
		return
			(lhsValue == rhsValue) ? 0 :
			(lhsValue > rhsValue) ? -1 :
			1;
	}
};


int main()
{



	return 0;
}
