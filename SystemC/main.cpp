#include <systemc.h>
#include <iostream>
#include <random>

using namespace std;

//===================interfaces=====================

class people_to_laboratory_if : public sc_interface {
public:
    virtual void get_human () = 0;
};

class laboratory_to_leagueVillians_if : public sc_interface {
public:
    virtual void become_a_villian (const int typeE)=0;
};

class laboratory_to_leagueHeroes_if : public sc_interface {
public:
    virtual void become_a_hero (const int typeH)=0;
};

class villain_to_importantObject_if : public sc_interface {
public:
    virtual void capture_object (const int powerE) = 0;
};

class importantObject_to_people_if : public sc_interface {
public:
    virtual void advanced_ultimatum (const int data) = 0;
};

class people_to_heroes_if : public sc_interface {
public:
    virtual void ask_help_from_heroes (const int powerE) = 0;
};

class heroes_to_importantObject_if : public sc_interface {
public:
    virtual void send_help_from_heroes (const int powerH) = 0;
};
//====================classes=======================

class people: public sc_module, public importantObject_to_people_if
{
public:
    sc_port<people_to_laboratory_if> tx_people_to_laboratory_port;
    sc_port<people_to_heroes_if> tx_people_to_heroes_port;

    SC_CTOR(people){
        cout<<"INFO \t Human was born!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        SC_THREAD(human_generator);
    }

    void human_generator (){
        //sleep(1);
        while (true) {
        cout<<"INFO \t New victim of the experiment!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        tx_people_to_laboratory_port->get_human();
        sleep(1);
        wait(3,SC_NS);
        }
    }

    void advanced_ultimatum(const int data)//Check !!!!we can add type object and power villain
    {
       // ask_for_help(data);
        /*if (data == 4)
        {
            cout<<"Out meet "<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        }*/
        cout<<"\t HEEELP!!! We need to help! \t "<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        tx_people_to_heroes_port->ask_help_from_heroes(data);
    }
};


class laboratory: public sc_module, public people_to_laboratory_if
{
public:
    sc_port<laboratory_to_leagueVillians_if> tx_laboratory_to_leagueVillians_port;
    sc_port<laboratory_to_leagueHeroes_if> tx_laboratory_to_leagueHeroes_port;

    sc_event e_creation;
    SC_CTOR(laboratory){
        cout<<"INFO \t Laboratory is start working!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        SC_METHOD(get_transformation);
        dont_initialize();
        sensitive<<e_creation;
    }

    void get_human(){
        cout<<" Meet new victim !\t"<<sc_time_stamp().to_string()<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
       // get_transformation();
        e_creation.notify(1,SC_NS);
    }

    void get_transformation(){
        int randtype;
        srand (time(0));
        randtype = 1+rand()%4;

        cout<<"Your transformation with help ";

        if(randtype==1)cout<<"radiation."<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(randtype==2)cout<<"a bite of an insect."<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(randtype==3)cout<<"acid."<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(randtype==4)cout<<"gene mutation."<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;

        int randCharacter;
        srand (time(0));
        randCharacter = 1+rand()%2;

        if(randCharacter==1)
        {
            cout<<"\tYou are evil! Go to the league of villains"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
            tx_laboratory_to_leagueVillians_port->become_a_villian(randtype);
        }
        else //if(randCharacter==2)
        {
            cout<<"\tYou are hero! Go to the league of heroes"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
            tx_laboratory_to_leagueHeroes_port->become_a_hero(randtype);
        }
    }
};

class heroes: public sc_module, public laboratory_to_leagueHeroes_if, public people_to_heroes_if
{
    int powerHero=0;

public:
    sc_event e_handle_hero;
    sc_port<heroes_to_importantObject_if> tx_heroes_to_importantObject_port;
    SC_CTOR(heroes){
        cout<<"INFO \t Heroes have power!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        SC_METHOD(create_power_hero);
       // SC_METHOD(ask_help_from_heroes);
        dont_initialize();
        sensitive<<e_handle_hero;
    }


    void create_power_hero(){
        srand (time(0));
        powerHero = 200+rand()%800;
        cout<<"Power hero is "<<powerHero<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
    }

    void ask_help_from_heroes(const int powerEvil)
    {
        if(powerHero!=0 && (powerEvil!=0))
        {
            while(powerEvil>=powerHero)
            {
                create_power_hero();
            }
             cout<<"Hero go with power "<<powerHero<<" that more than power villain "<<powerEvil<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
             tx_heroes_to_importantObject_port->send_help_from_heroes(powerHero);
        }

    }

    void become_a_hero(const int typeH)
    {
        if(typeH==1)cout<<"Now you are radiation human. Your mentor will be Hulk. Congratulations!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(typeH==2)cout<<"Now you are an insect human. Your mentor will be Spiderman. Congratulations! "<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(typeH==3)cout<<"Now you are a acid human. Your mentor will be  Martian Manhunter.Congratulations!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(typeH==4)cout<<"Now you are a mutant! Your mentor will be Professor X. Congratulations! "<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        e_handle_hero.notify(1,SC_NS);
    }
};

class villain:public sc_module, public laboratory_to_leagueVillians_if
{
    int powerEvil;
public:
    sc_event e_creation_evil;
    sc_port<villain_to_importantObject_if> tx_villain_to_importantObject_port;

    SC_CTOR(villain){
        cout<<"INFO \t Villain have power!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        SC_METHOD(evil_capture_object);
        dont_initialize();
        sensitive<<e_creation_evil;
    }


    void evil_capture_object()
    {
        srand (time(0));
        powerEvil = 1+rand()%300;
        cout<<"Power evil is "<<powerEvil<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        tx_villain_to_importantObject_port->capture_object(powerEvil);
    }

    void become_a_villian(const int typeE)
    {
        if(typeE==1)cout<<"Now you are radiation human. Your mentor will be Mr. Freeze. Congratulations!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(typeE==2)cout<<"Now you are an insect human. Your mentor will be Scorpio (real name - Mac Gargan). Congratulations! "<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(typeE==3)cout<<"Now you are a acid human. Your mentor will be Harley Quinn. Congratulations!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(typeE==4)cout<<"Now you are a mutant! Your mentor will be Magneto. Congratulations! "<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        e_creation_evil.notify(1,SC_NS);
    }

};

class importantObjects:public sc_module,public heroes_to_importantObject_if, public villain_to_importantObject_if
{
    int pEvil;
    int powerHero;
public:
    sc_event e_handle;
    sc_port<importantObject_to_people_if> tx_importantObject_to_people_port;
    SC_CTOR(importantObjects){
        cout<<"INFO \t Important Object was created!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        SC_METHOD(wait_capture_and_ask_for_help);
        dont_initialize();
        sensitive<<e_handle;
    }

    void wait_capture_and_ask_for_help()
    {
      //  cout<<"\t Sending a request for help!!!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        cout<<"\t Send an ultimatum   E==="<<pEvil<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        tx_importantObject_to_people_port->advanced_ultimatum(pEvil);
    }

    void send_help_from_heroes(const int powerHero)
    {
        cout<<"!!! The Hero is here! His power = "<<powerHero<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
    }

    void capture_object(const int powerEvil)
    {
        int randObj;
        srand (time(0));
        randObj = 1+rand()%4;
        pEvil=powerEvil;
        if(randObj==1)cout<<"\t Gold was captured!! Power Evil = "<<powerEvil<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(randObj==2)cout<<"\t Museum was captured!! Power Evil = "<<powerEvil<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(randObj==3)cout<<"\t Jewelry shop was captured!! Power Evil = "<<powerEvil<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        if(randObj==4)cout<<"\t Some Important Object was captured!! Power Evil = "<<powerEvil<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        //cout<<"\t This object was captured!!!! Power Evil = "<<powerEvil<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;
        e_handle.notify(1,SC_NS);
    }

};


class hero_and_villain: public sc_module {
public:
    people u_people;
    laboratory u_laboratory;
    heroes u_heroes;
    villain u_villain;
    importantObjects u_importantObjects;

    SC_CTOR(hero_and_villain): u_people("people"),u_laboratory("laboratory"), u_heroes("heroes"), u_villain("villain"), u_importantObjects("importantObjects")
    {
        cout<<"INFO \t Our universe was opened!"<<"------------------------------------ "<<sc_time_stamp().to_string()<<endl;

        u_people.tx_people_to_laboratory_port(u_laboratory);
        u_people.tx_people_to_heroes_port(u_heroes);

        u_laboratory.tx_laboratory_to_leagueHeroes_port(u_heroes);
        u_laboratory.tx_laboratory_to_leagueVillians_port(u_villain);

        u_heroes.tx_heroes_to_importantObject_port(u_importantObjects);

        u_villain.tx_villain_to_importantObject_port(u_importantObjects);

        u_importantObjects.tx_importantObject_to_people_port(u_people);
    }
};

//======================main========================

int sc_main (int argc, char *argv[])
{
    hero_and_villain Our_universe ("Universe_Our_universe");
    sc_start(15, SC_NS);
    return 0;
}


