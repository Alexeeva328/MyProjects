using GalaSoft.MvvmLight;
using System.Collections.Generic;
using System.Xml;
using System.Collections.ObjectModel;
using Microsoft.Win32;
using System.IO;


namespace WpfApp.ViewModel
{
    /// <summary>
    /// This class contains properties that the main View can data bind to.
    /// <para>
    /// Use the <strong>mvvminpc</strong> snippet to add bindable properties to this ViewModel.
    /// </para>
    /// <para>
    /// You can also use Blend to data bind with the tool's support.
    /// </para>
    /// <para>
    /// See http://www.galasoft.ch/mvvm
    /// </para>
    /// </summary>
    public class MainViewModel : ViewModelBase
    {
        
        private ObservableCollection<Human> list_hum;

        public ObservableCollection<Human> HelloWorld
        {
            get
            {
                return list_hum;
            }
            set
            {
                Set(() => HelloWorld, ref list_hum, value);
            }
        }


        /// <summary>
        /// Initializes a new instance of the MainViewModel class.
        /// </summary>
        public MainViewModel()
        {
           
        }

        public ObservableCollection<Human> Load_xml()
        {
            ObservableCollection<Human> New_humans = new ObservableCollection<Human>();
            XmlDocument xDoc = new XmlDocument();

            string FilePath;
            OpenFileDialog openFileDialog = new OpenFileDialog();
            if (openFileDialog.ShowDialog() == true)
            {
                FilePath = openFileDialog.FileName;
            }
                        
            xDoc.Load(openFileDialog.FileName.ToString());
            // получим корневой элемент
            XmlElement xRoot = xDoc.DocumentElement;
            // обход всех узлов в корневом элементе
            foreach (XmlNode xnode in xRoot)
            {
                Human h = new Human();
                if (xnode.Attributes.Count > 0)
                {
                    XmlNode attr = xnode.Attributes.GetNamedItem("Name");
                    if (attr != null)
                    {
                        //New_humans.Add(new Human { Name = attr.Value.ToString() });
                        h.Name = attr.Value.ToString();
                    }
                }
                foreach (XmlNode childnode in xnode.ChildNodes)
                {
                    if (childnode.Name == "Patronym")
                    {
                        h.Patronym = childnode.InnerText;
                    }
                    if (childnode.Name == "LName")
                    {
                        h.LName = childnode.InnerText;
                    }
                     if (childnode.Name == "Email")
                    {
                        h.Email = childnode.InnerText;
                    }
                }
                New_humans.Add(new Human {Name =h.Name, Patronym = h.Patronym, LName = h.LName, Email = h.Email});
            }
            return New_humans;
        }

        public void Add_new_human(string new_name, string new_patr, string new_lastname, string new_email, ObservableCollection<Human> all_humans)
        {
            all_humans.Add(new Human { Name = new_name, Patronym = new_patr, LName = new_lastname, Email = new_email});
        }

        public void Save_xml(ObservableCollection<Human> humans)
        {
            ObservableCollection<Human> New_humans = new ObservableCollection<Human>();
            XmlDocument xDoc = new XmlDocument();
            XmlNode docNode = xDoc.CreateXmlDeclaration("1.0", "UTF-8", null);
            xDoc.AppendChild(docNode);

            XmlElement xRoot_one = xDoc.CreateElement("users");
            xDoc.AppendChild(xRoot_one);
            XmlElement xRoot = xDoc.DocumentElement;

            SaveFileDialog dialog = new SaveFileDialog();
            dialog.DefaultExt = ".xml";
            dialog.FileName = "Saved_humans";

            
            foreach (var hum in humans)
            {
                // создаем новый элемент 
                XmlElement userElem = xDoc.CreateElement("Human");
                XmlAttribute nameAttr = xDoc.CreateAttribute("Name");
                XmlElement PatronymElem = xDoc.CreateElement("Patronym");
                XmlElement LNameElem = xDoc.CreateElement("LName");
                XmlElement EmailElem = xDoc.CreateElement("Email");
                // создаем текстовые значения для элементов и атрибута
                XmlText nameText = xDoc.CreateTextNode(hum.Name);
                XmlText PatronymText = xDoc.CreateTextNode(hum.Patronym);
                XmlText LNameText = xDoc.CreateTextNode(hum.LName);
                XmlText EmailText = xDoc.CreateTextNode(hum.Email);


                //добавляем узлы
                nameAttr.AppendChild(nameText);
                PatronymElem.AppendChild(PatronymText);
                LNameElem.AppendChild(LNameText);
                EmailElem.AppendChild(EmailText);

                userElem.Attributes.Append(nameAttr);
                userElem.AppendChild(PatronymElem);
                userElem.AppendChild(LNameElem);
                userElem.AppendChild(EmailElem);

                xRoot.AppendChild(userElem);
            }
            
            if (dialog.ShowDialog() == true)
            {
                xDoc.Save(dialog.FileName.ToString());
            }


        }
    }
}