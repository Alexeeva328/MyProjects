using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Collections.ObjectModel;
using System.Xml;


namespace WpfApp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public ObservableCollection<ViewModel.Human> humans;

        public MainWindow()
        {
            InitializeComponent();
             humans = new ObservableCollection<ViewModel.Human>
            {
                new ViewModel.Human {Name = "Nana", Patronym = "Tomich", LName = "Patterson", Email = "Patterson@mail.ru"},
                new ViewModel.Human {Name = "Jina", Patronym = "Rich", LName = "Dotcom", Email = "Rich.com"}

            };
             humansGrid.DataContext = humans;
        }

        private void Add_Button_Click(object sender, RoutedEventArgs e)
        {
            //MessageBox.Show("Добавление новой записи");
            var DataContextdf = new ViewModel.MainViewModel();
            DataContextdf.Add_new_human(NewName.Text.ToString(), NewPatr.Text.ToString(), NewLastName.Text.ToString(), NewEmailAdress.Text.ToString(),humans);
        }

        private void Delete_Button_Click(object sender, RoutedEventArgs e)
        {
            //MessageBox.Show("Удаление последней записи");
            if (humans.Count()!=0)
                humans.Remove(humans.Last());
        }

        private void Save_Button_Click(object sender, RoutedEventArgs e)
        {

            var DataContextdf = new ViewModel.MainViewModel();
            DataContextdf.Save_xml(humans);
        }

        private void Load_Button_Click(object sender, RoutedEventArgs e)
        {
            //MessageBox.Show("Загрузка данных из xml");
            var DataContextdf = new ViewModel.MainViewModel();
            
            humans.Clear();
            humans = DataContextdf.Load_xml();

            humansGrid.DataContext = humans;
        }
    }
}
