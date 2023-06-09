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
    public partial class New : Form
    {
        public New()
        {
            InitializeComponent();
            Posts();
        }

        private void Back_Click(object sender, EventArgs e)
        {
            Main_form mm = new Main_form();
            mm.Show();
            this.Hide();
        }

        private void New_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.ExitThread();
        }

        private void ButtonNew_Click(object sender, EventArgs e)
        {
            if (String.IsNullOrWhiteSpace(FIO.Text) || String.IsNullOrWhiteSpace(Login.Text) || String.IsNullOrWhiteSpace(Password.Text) || String.IsNullOrWhiteSpace(Post.Text))
            {
                MessageBox.Show("Заполните все поля");
            }
            else
            {
                SqlConnection SqlConnect = new SqlConnection(@"Data Source=kp11.ru,7777;Initial Catalog=ShuvalovGleb;User ID=kekwsr;Password=Cisco123$");
                SqlConnect.Open();
                SqlCommand sqlQuery = new SqlCommand(@"INSERT INTO [dbo].[Employees](Name, Login, Password, Date, Post) VALUES ('" + Convert.ToString(FIO.Text) + "', '" + Convert.ToString(Login.Text) + "', '" + Convert.ToString(Password.Text) + "', '" + DateTime.Now.ToString("MM.dd.yyyy") + "', '" + Convert.ToString(Post.Text) + "')", SqlConnect);
                sqlQuery.ExecuteNonQuery();
                MessageBox.Show("Вы внесли нового сотрудника в базу данных!");
                Post.Items.Clear();
                Post.Text = "";
                Login.Text = "";
                Password.Text = "";
                FIO.Text = "";
                Posts();
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
    }
}
