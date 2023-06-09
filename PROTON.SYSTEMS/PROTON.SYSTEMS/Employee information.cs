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
    public partial class Employee_information : Form
    {
        public Employee_information()
        {
            InitializeComponent();
            Humans();
            ViewList();
        }

        private void Back_Click(object sender, EventArgs e)
        {
            Main_form mm = new Main_form();
            mm.Show();
            this.Hide();
        }

        private void Employee_information_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.ExitThread();
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

        private void ChangeHuman_SelectedIndexChanged(object sender, EventArgs e)
        {
            SqlConnection sqlConnect1 = new SqlConnection(@"Data Source=kp11.ru,7777;Initial Catalog=ShuvalovGleb;User ID=kekwsr;Password=Cisco123$");
            sqlConnect1.Open();
            SqlCommand sqlView = new SqlCommand(@"Select * from [dbo].[Employees] where Name = '" + Convert.ToString(ChangeHuman.Text) + "' ", sqlConnect1);
            SqlDataReader sqlReader = null;
            sqlReader = sqlView.ExecuteReader();
            if (sqlReader.Read())
            {
                label8.Text = Convert.ToString(sqlReader[1]);
                label9.Text = Convert.ToString(sqlReader[2]);
                label10.Text = Convert.ToString(sqlReader[3]);
                label11.Text = Convert.ToString(sqlReader[4]);
                label12.Text = Convert.ToString(sqlReader[5]);
            }
            else
            {
                MessageBox.Show("Данных нет!");
            }
        }
        public void ViewList()
        {
            SqlConnection sqlConnect2 = new SqlConnection(@"Data Source=kp11.ru,7777;Initial Catalog=ShuvalovGleb;User ID=kekwsr;Password=Cisco123$");
            sqlConnect2.Open();
            SqlCommand sqlView = new SqlCommand(@"Select * From [dbo].[Employees]", sqlConnect2);
            SqlDataReader sqlReader = null;
            sqlReader = sqlView.ExecuteReader();

            while (sqlReader.Read())
            {
                ListViewItem lw = new ListViewItem(new string[] {
                Convert.ToString(sqlReader[1]),
                Convert.ToString(sqlReader[2]),
                Convert.ToString(sqlReader[3]),
                Convert.ToString(sqlReader[4]),
                Convert.ToString(sqlReader[5])
            });

                listView1.Items.Add(lw);
            }
        }
    }
}
