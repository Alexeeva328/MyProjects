using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using GalaSoft.MvvmLight;


namespace WpfApp.ViewModel
{
    public class Human : ObservableObject
    {
        private string firstName;  //имя
        private string patronymic;   //отчество
        private string lastName;  //фамилия
        private string email;
        
        public string Name
        {
            get
            {
                return firstName;
            }
            set
            {
                Set<string>(() => this.Name, ref firstName, value);
            }
        }

        public string Patronym
        {
            get
            {
                return patronymic;
            }
            set
            {
                Set<string>(() => this.Patronym, ref patronymic, value);
            }
        }

        public string LName
        {
            get
            {
                return lastName;
            }
            set
            {
                Set<string>(() => this.Name, ref lastName, value);
            }
        }

        public string Email
        {
            get
            {
                return email;
            }
            set
            {
                Set<string>(() => this.Email, ref email, value);
            }
        }

        public List<Human> GetHuman()
        {
            List<Human> humans = new List<Human>
            {
                new Human {Name = "NNana", Patronym = "Tomich", LName = "Patterson", Email = "Patterson@mail.ru"},
                new Human {Name = "JJina", Patronym = "Rich", LName = "Dotcom", Email = "Rich.com"}

            };
            
            return humans;
        }
    }
}
