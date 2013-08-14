#include <iostream>
#include <string>

class Foods
{
private:

	std::string name_;
	double amount_;
	double quality_;

public:

	Foods(const std::string name, double amount, double quality)
		: name_(name)
		, amount_(amount)
		, quality_(quality)
	{
	}

	virtual std::string getName() const
	{
		return name_;
	}

	virtual double getAmount() const
	{
		return amount_;
	}

	virtual double getQuality() const
	{
		return quality_;
	}
};


class FoodsComparator
{
public:

    virtual int compare(const Foods& lhs, const Foods& rhs) = 0;
};

class KouchanComparator
	: public FoodsComparator
{
public:

    int compare(const Foods& lhs, const Foods& rhs)
	{
		// こうちゃんは、量2割 味8割
		double lhsValue = lhs.getAmount() * 0.2 + lhs.getQuality() * 0.8;
		double rhsValue = rhs.getAmount() * 0.2 + rhs.getQuality() * 0.8;
		return
			(lhsValue == rhsValue) ? 0 :
			(lhsValue > rhsValue) ? -1 :
			1;
	}
};


class LenokunComparator
	: public FoodsComparator
{
public:

    int compare(const Foods& lhs, const Foods& rhs)
	{
		// レノくんは、量8割 味2割
		double lhsValue = lhs.getAmount() * 0.8 + lhs.getQuality() * 0.2;
		double rhsValue = rhs.getAmount() * 0.8 + rhs.getQuality() * 0.2;
		return
			(lhsValue == rhsValue) ? 0 :
			(lhsValue > rhsValue) ? -1 :
			1;
	}
};

class LanchMenu
{
private:
	FoodsComparator* comparator_;
	Foods aLanch_;
	Foods bLanch_;
	Foods uraLanch_;
public:

	LanchMenu(FoodsComparator* comparator)
	    : comparator_(comparator)  
		, aLanch_("A Lanch", 100, 50)
		, bLanch_("B Lanch", 50, 100)
		, uraLanch_("Ura Lanch", 100, 100)
	{
	}
	virtual Foods provide()
	{
		if(comparator_->compare(aLanch_, bLanch_) == -1) {
			return aLanch_;
		}
		else if(comparator_->compare(aLanch_, bLanch_) == 1) {
			return bLanch_;
		}
		return uraLanch_;
	}
	
};

int main()
{
	{
		KouchanComparator* kouchanComparator = new KouchanComparator;
		LanchMenu lanchMenu(kouchanComparator);
		std::cout << lanchMenu.provide().getName() << std::endl;
		delete kouchanComparator;
	}
		
	{
		LenokunComparator* lenokunComparator = new LenokunComparator;
		LanchMenu lanchMenu(lenokunComparator);
		std::cout << lanchMenu.provide().getName() << std::endl;
		delete lenokunComparator;
	}

	return 0;
}
