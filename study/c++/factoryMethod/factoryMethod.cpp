// compile : g++ factoryMethod.cpp -o factoryMethod.bin && ./factoryMethod.bin

#include <iostream>

class Material
{
public:
	virtual std::string getName() = 0;
};

class Lunch
{
public:

	virtual Material* createMaterial() = 0;
	virtual void prepare(Material* material) = 0;
	virtual void make(Material* material) = 0;
	virtual void eat(Material* material) = 0;

	virtual void createLunch()
	{
		Material * material = createMaterial();

		prepare(material);
		make(material);
		eat(material);

		delete material;
	}
};


class Rice : public Material
{
public:
	virtual std::string getName()
	{
		return "ごはん";
	}
};

class Catfood : public Material
{
public:
	virtual std::string getName()
	{
		return "キャットフード";
	}
};

class KouchanLunch : public Lunch
{
	virtual Material* createMaterial()
	{
		return new Rice;
	}
	virtual void prepare(Material* material)
	{
		std::cout << material->getName() << "炊きます。" << std::endl;
	}
	virtual void make(Material* material)
	{
		std::cout << "茶碗に盛ります。" << std::endl;
	}
	virtual void eat(Material* material)
	{
		std::cout << "いただきます。" << std::endl;
	}
};

class RenoLunch : public Lunch
{
	virtual Material* createMaterial()
	{
		return new Catfood;
	}
	virtual void prepare(Material* material)
	{
		std::cout << material->getName() << "を開けます" << std::endl;
	}
	virtual void make(Material* material)
	{
		std::cout << "ご飯皿に盛ります。" << std::endl;
	}
	virtual void eat(Material* material)
	{
		std::cout << "にゃにゃにゃ" << std::endl;
	}
};

int main()
{
    Lunch* lunch;

	lunch = new  KouchanLunch;
	lunch->createLunch();
	delete lunch;

	lunch = new  RenoLunch;
	lunch->createLunch();
	delete lunch;

	return 0;
}
