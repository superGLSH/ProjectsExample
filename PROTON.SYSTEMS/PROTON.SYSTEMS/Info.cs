﻿using System;
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
    public partial class Info : Form
    {
        public Info()
        {
            InitializeComponent();
        }

        private void Info_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.ExitThread();
        }

        private void Back_Click(object sender, EventArgs e)
        {
            Main_form mm = new Main_form();
            mm.Show();
            this.Hide();
        }
    }
}
