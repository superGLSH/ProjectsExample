using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace PROTON.SYSTEMS
{
    public partial class Change : Form
    {
        public Change()
        {
            InitializeComponent();
            Humans();
        }
        private void Back_Click(object sender, EventArgs e)
        {
            Main_form mm = new Main_form();
            mm.Show();
            this.Hide();
        }

        private void Change_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.ExitThread();
        }

        private void ButtonChange_Click(object sender, EventArgs e)
        {
            if (String.IsNullOrWhiteSpace(ChangeHuman.Text) || String.IsNullOrWhiteSpace(FIO.Text) || String.IsNullOrWhiteSpace(Login.Text) || String.IsNullOrWhiteSpace(Password.Text) || String.IsNullOrWhiteSpace(Post.Text))
            {
                MessageBox.Show("Некоторые поля не заполнены!");
            }
            else
            {
                SqlConnection SqlConnect = new SqlConnection(@"Data Source=kp11.ru,7777;Initial Catalog=ShuvalovGleb;User ID=kekwsr;Password=Cisco123$");
                SqlConnect.Open();
                SqlCommand sqlUp = new SqlCommand(@"UPDATE [dbo].[Employees] SET Name='"+Convert.ToString(FIO.Text)+"', Login='"+ Convert.ToString(Login.Text) + "', Password='"+ Convert.ToString(Password.Text) + "', Date='"+ DateTime.Now.ToString("MM.dd.yyyy") + "', Post ='"+ Convert.ToString(Post.Text) + "' where Name='"+Convert.ToString(ChangeHuman.Text)+"'", SqlConnect);
                sqlUp.ExecuteNonQuery();
                MessageBox.Show("Вы обновили данные о сотруднике!");
                ChangeHuman.Items.Clear();
                ChangeHuman.Text = "";
                Post.Items.Clear();
                Post.Text = "";
                Login.Text = "";
                Password.Text = "";
                FIO.Text = "";
                Humans();
            }
        }
        private void Humans()
        {
            SqlConnection SqlConnect0 = new SqlConnection(@"Data Source=kp11.ru,7777;Initial Catalog=ShuvalovGleb;User ID=kekwsr;Password=Cisco123$");
            SqlConnect0.Open();
            SqlCommand sqlView = new SqlCommand(@"Select Name From [dbo].Employees", SqlConnect0);
            SqlDataReader sqlReader = null;
            sqlReader = sqlView.ExecuteReader();
            while (sqlReader.Read())
            {
                ChangeHuman.Items.Add(sqlReader["Name"]);
            }
        }
        public void Posts()
        {
            SqlConnection SqlConnect0 = new SqlConnection(@"Data Source=kp11.ru,7777;Initial Catalog=ShuvalovGleb;User ID=kekwsr;Password=Cisco123$");
            SqlConnect0.Open();
            SqlCommand sqlView = new SqlCommand(@"Select Post From [dbo].Post", SqlConnect0);
            SqlDataReader sqlReader = null;
            sqlReader = sqlView.ExecuteReader();
            while (sqlReader.Read())
            {
                Post.Items.Add(sqlReader["Post"]);
            }
        }

        private void ChangeHuman_SelectedIndexChanged(object sender, EventArgs e)
        {
            SqlConnection sqlConnect1 = new SqlConnection(@"Data Source=kp11.ru,7777;Initial Catalog=ShuvalovGleb;User ID=kekwsr;Password=Cisco123$");
            sqlConnect1.Open();
            SqlCommand sqlView = new SqlCommand(@"Select * from [dbo].[Employees] where Name = '" + Convert.ToString(ChangeHuman.Text) + "' ", sqlConnect1);
            SqlDataReader sqlReader = null;
            sqlReader = sqlView.ExecuteReader();
            if (sqlReader.Read())
            {
                FIO.Text = Convert.ToString(sqlReader[1]);
                Login.Text = Convert.ToString(sqlReader[2]);
                Password.Text = Convert.ToString(sqlReader[3]);
                Post.Text =Convert.ToString(sqlReader[5]);
                Posts();
            }
            else
            {
                MessageBox.Show("Данных нет!");
            }
        }
    }
}
