using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace PROTON.SYSTEMS
{
    public partial class Main_form : Form
    {
        public Main_form()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Employee_information ei = new Employee_information();
            ei.Show();
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            New n = new New();
            n.Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Change c = new Change();
            c.Show();
            this.Hide();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Delete d = new Delete();
            d.Show();
            this.Hide();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            FAQ f = new FAQ();
            f.Show();
            this.Hide();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Info i = new Info();
            i.Show();
            this.Hide();
        }

        private void Main_form_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.ExitThread();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            Application.ExitThread();
        }
    }
}
