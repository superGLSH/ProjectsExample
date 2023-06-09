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
    public partial class Delete : Form
    {
        public Delete()
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

        private void Delete_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.ExitThread();
        }

        private void ButtonDelete_Click(object sender, EventArgs e)
        {
            if (String.IsNullOrWhiteSpace(ChangeHuman.Text))
            {
                MessageBox.Show("Выберите сотрудника!");
            }
            else
            {
                SqlConnection SqlConnect = new SqlConnection(@"Data Source=kp11.ru,7777;Initial Catalog=ShuvalovGleb;User ID=kekwsr;Password=Cisco123$");
                SqlConnect.Open();
                SqlCommand sqlUp = new SqlCommand(@"DELETE FROM [dbo].[Employees] where Name='" + Convert.ToString(ChangeHuman.Text) + "'",SqlConnect);
                sqlUp.ExecuteNonQuery();
                MessageBox.Show("Вы удалили сотрудника из базы данных!");
                ChangeHuman.Items.Clear();
                ChangeHuman.Text = "";
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
    }
}
