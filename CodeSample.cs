namespace Solarsoft.Utilities.EventViewerAdmin
{
        #region opening file

        // used at start of program
        public void recentFileTxt()
        {
            // create file if it does not exist
            using (StreamWriter file_check = File.AppendText(@"C:\recentfiles.txt"))
            {
                string nullstring = null;
                file_check.Write(nullstring);
            }


            // READ RECENTFILES.TXT
            string[] recentFiles = new string[6];

            using (System.IO.StreamReader file_r = new System.IO.StreamReader(@"C:\recentfiles.txt", true))
            {
                // store the unique recent files
                for (int i = 0; i < 6; i++)
                { recentFiles[i] = file_r.ReadLine(); }
            }


            // POPULATE: FILE >> RECENT FILES
            recentfile1ToolStripMenuItem.Text = recentFiles[0];
            recentfile2ToolStripMenuItem.Text = recentFiles[1];
            recentfile3ToolStripMenuItem.Text = recentFiles[2];
            recentfile4ToolStripMenuItem.Text = recentFiles[3];
            recentfile5ToolStripMenuItem.Text = recentFiles[4];
            recentfile6ToolStripMenuItem.Text = recentFiles[5];

            // disable recentfile-menuitems with no text
            // note: first if-else does not include ".Visible=false" - if there are no recent files, it will show a blank box inside Recent Files
            if (recentfile1ToolStripMenuItem.Text == null) { /*recentfile1ToolStripMenuItem.Visible = false;*/ recentfile1ToolStripMenuItem.Enabled = false; }
            else { recentfile1ToolStripMenuItem.Visible = true; recentfile1ToolStripMenuItem.Enabled = true; }

            if (recentfile2ToolStripMenuItem.Text == null) { recentfile2ToolStripMenuItem.Visible = false; recentfile2ToolStripMenuItem.Enabled = false; }
            else { recentfile2ToolStripMenuItem.Visible = true; recentfile2ToolStripMenuItem.Enabled = true; }

            if (recentfile3ToolStripMenuItem.Text == null) { recentfile3ToolStripMenuItem.Visible = false; recentfile3ToolStripMenuItem.Enabled = false; }
            else { recentfile3ToolStripMenuItem.Visible = true; recentfile3ToolStripMenuItem.Enabled = true; }

            if (recentfile4ToolStripMenuItem.Text == null) { recentfile4ToolStripMenuItem.Visible = false; recentfile4ToolStripMenuItem.Enabled = false; }
            else { recentfile4ToolStripMenuItem.Visible = true; recentfile4ToolStripMenuItem.Enabled = true; }

            if (recentfile5ToolStripMenuItem.Text == null) { recentfile5ToolStripMenuItem.Visible = false; recentfile5ToolStripMenuItem.Enabled = false; }
            else { recentfile5ToolStripMenuItem.Visible = true; recentfile5ToolStripMenuItem.Enabled = true; }

            if (recentfile6ToolStripMenuItem.Text == null) { recentfile6ToolStripMenuItem.Visible = false; recentfile6ToolStripMenuItem.Enabled = false; }
            else { recentfile6ToolStripMenuItem.Visible = true; recentfile6ToolStripMenuItem.Enabled = true; }

        }


        // updates toolbar >> File >> Recent Files
        //    argument: path of xml file opened/saved
        //    used for File >> Open, Save
        public void recentFileTxt(string xmlFilePath)
        {

            // create file if it does not exist
            using (StreamWriter file_check = File.AppendText(@"C:\recentfiles.txt"))
            {
                string nullstring = null;
                file_check.Write(nullstring);
            }

            // READ RECENTFILES.TXT (unique paths only)
            string[] recentFiles = new string[6];

            using (System.IO.StreamReader file_r = new System.IO.StreamReader(@"C:\recentfiles.txt", true))
            {
                // store opened file to array spot 1 of 6
                recentFiles[0] = xmlFilePath;

                // store the unique recent files into array spots 2-6 of 6
                for (int i = 1; i < 6; i++)
                {
                    string temp;
                    temp = file_r.ReadLine();

                    // if unique path, add to recentFiles
                    if (temp != xmlFilePath)
                    { recentFiles[i] = temp; }

                    // if not unique path, disregard path. in next loop-iteration, assign next string to current recentFiles
                    else
                    { i--; }
                }
            }

            // WRITE RECENTFILES.TXT
            string rfintro = "";
            System.IO.File.WriteAllText(@"C:\recentfiles.txt", rfintro);

            using (System.IO.StreamWriter file_w = new System.IO.StreamWriter(@"C:\recentfiles.txt", true))
            {
                // write 6 recent files to recentfiles.txt
                for (int i = 0; i < 6; i++)
                {
                    if (recentFiles[i] != null) // do not write if array-content is trivial
                    { file_w.WriteLine(recentFiles[i]); }
                }
            }

            // POPULATE: FILE >> RECENT FILES
            recentfile1ToolStripMenuItem.Text = recentFiles[0];
            recentfile2ToolStripMenuItem.Text = recentFiles[1];
            recentfile3ToolStripMenuItem.Text = recentFiles[2];
            recentfile4ToolStripMenuItem.Text = recentFiles[3];
            recentfile5ToolStripMenuItem.Text = recentFiles[4];
            recentfile6ToolStripMenuItem.Text = recentFiles[5];

            // disable recentfile-menuitems with no text
            // note: first if-else does not include ".Visible=false" - if there are no recent files, it will show a blank box inside Recent Files
            if (recentfile1ToolStripMenuItem.Text == null) { /*recentfile1ToolStripMenuItem.Visible = false;*/ recentfile1ToolStripMenuItem.Enabled = false; Console.WriteLine("1 disable"); }
            else { recentfile1ToolStripMenuItem.Visible = true; recentfile1ToolStripMenuItem.Enabled = true; Console.WriteLine("1 enable"); }

            if (recentfile2ToolStripMenuItem.Text == null) { recentfile2ToolStripMenuItem.Visible = false; recentfile2ToolStripMenuItem.Enabled = false; Console.WriteLine("2 disable"); }
            else { recentfile2ToolStripMenuItem.Visible = true; recentfile2ToolStripMenuItem.Enabled = true; Console.WriteLine("2 enable"); }

            if (recentfile3ToolStripMenuItem.Text == null) { recentfile3ToolStripMenuItem.Visible = false; recentfile3ToolStripMenuItem.Enabled = false; Console.WriteLine("3 disable"); }
            else { recentfile3ToolStripMenuItem.Visible = true; recentfile3ToolStripMenuItem.Enabled = true; Console.WriteLine("3 enable"); }

            if (recentfile4ToolStripMenuItem.Text == null) { recentfile4ToolStripMenuItem.Visible = false; recentfile4ToolStripMenuItem.Enabled = false; Console.WriteLine("4 disable"); }
            else { recentfile4ToolStripMenuItem.Visible = true; recentfile4ToolStripMenuItem.Enabled = true; Console.WriteLine("4 enable"); }

            if (recentfile5ToolStripMenuItem.Text == null) { recentfile5ToolStripMenuItem.Visible = false; recentfile5ToolStripMenuItem.Enabled = false; Console.WriteLine("5 disable"); }
            else { recentfile5ToolStripMenuItem.Visible = true; recentfile5ToolStripMenuItem.Enabled = true; Console.WriteLine("5 enable"); }

            if (recentfile6ToolStripMenuItem.Text == null) { recentfile6ToolStripMenuItem.Visible = false; recentfile6ToolStripMenuItem.Enabled = false; Console.WriteLine("6 disable"); }
            else { recentfile6ToolStripMenuItem.Visible = true; recentfile6ToolStripMenuItem.Enabled = true; Console.WriteLine("6 enable"); }

        }


        // Open .xml File for: toolbar >> File >> Open
        public void openEventViewerConfig(string xmlFilePath)
        {
            workPath = xmlFilePath;
            // Check if file does not exist
            if (!File.Exists(workPath))
            {
                MessageBox.Show("The file " + workPath + " cannot be opened.",
                "Solarsoft Event Viewer", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                if (!ConfirmUnsavedChanges()) // confirm that the user wants to save first
                    return;                   // - if user chooses cancel, then stop

                // reset current and active tree nodes
                currentLogNode = -1;
                currentSourceNode = -1;
                activeLogNode = -1;
                activeSourceNode = -1;

                UpdateMessageList(); // update datagrid

                xmlCfg = new EventViewerConfig();
                xmlCfg = DeserializeFromXML(workPath); // store/deserialize the xml data to the event viewer object
                savedCfg = new EventViewerConfig(xmlCfg); // record saved event viewer config object

                ResetMenuStrip(); // reset main menu strip since there is no active source
                tvEventViewer.Nodes[0].Nodes.Clear(); // clear the current tree
                UpdateTreeView(xmlCfg, tvEventViewer); // update file tree
            }
        }

        #endregion
		
		#region Treeview

        // Arguments: EventViewerConfig and TreeView objects
        // Updates the TreeView to represent the data contained in EventViewerConfig:
        // - updates TreeView-Logs
        //      - updates TreeView-Sources
        //      - deletes extraneous TreeView-Sources
        // - deletes extraneous TreeView-Logs
        public void UpdateTreeView(EventViewerConfig eventData, TreeView treeDisplay)
        {

            /* ========================================== TreeView-Logs ============================================= */

            // Loops through EventViewerConfig-logs
            // Updates the names of the TreeView-logs to match EventViewerConfig-logs
            // Nested for-loop: similar updates for sources
            for (int intlogs = 0; intlogs < eventData.eventLogs.Count; intlogs++)
            {

                /* =================== Check if TreeView-Log Update Required =================== */

                bool needLogUpdate = false;

                // TreeView update required if EventViewerConfig-logname does not match TreeView-logname
                if (intlogs < treeDisplay.Nodes[0].Nodes.Count) // only compare if in array range
                {
                    if (treeDisplay.Nodes[0].Nodes[intlogs].Text != eventData.eventLogs[intlogs].eventLogName)
                    { needLogUpdate = true; }
                }

                // TreeView update required if index-intlogs greater than TreeView-logs
                if (intlogs >= treeDisplay.Nodes[0].Nodes.Count)
                { needLogUpdate = true; }

                /* ============================================================================= */



                /* =================== Edit TreeView (Logs) =================== */

                if (needLogUpdate == true)
                {
                    TreeNode templognode = new TreeNode(eventData.eventLogs[intlogs].eventLogName);

                    // Set Log Icon
                    templognode.ImageIndex = 2;
                    templognode.SelectedImageIndex = 2;

                    // if # logs: eventViewerConfig < TreeView, perform delete on TreeView at index-intlogs 
                    if (eventData.eventLogs.Count < treeDisplay.Nodes[0].Nodes.Count)
                    {
                        treeDisplay.Nodes[0].Nodes[intlogs].Remove(); // Removes the non-match log-node in TreeView
                    }

                    // if # logs: eventViewerConfig = TreeView, perform rename on TreeView at index-intlogs
                    else if (eventData.eventLogs.Count == treeDisplay.Nodes[0].Nodes.Count)
                    {
                        treeDisplay.Nodes[0].Nodes[intlogs].Text = eventData.eventLogs[intlogs].eventLogName; // Renames the non-match log-node in TreeView
                    }

                    // if # logs: eventViewerConfig > TreeView, perform insert on TreeView at index-intlogs
                    else if (eventData.eventLogs.Count > treeDisplay.Nodes[0].Nodes.Count)
                    {
                        treeDisplay.Nodes[0].Nodes.Insert(intlogs, templognode); // Add eventViewerConfig log to TreeView
                    }

                }

                /* =========================================================== */



                /* ======================================= TreeView-Sources ===================================== */

                // Loops through EventViewerConfig-sources
                // Updates EventViewerConfig-sources for a TreeView-log
                for (int intsources = 0; intsources < eventData.eventLogs[intlogs].sources.Count; intsources++)
                {
                    /* =================== Check if TreeView-Source Update Required =================== */
                    bool needSourceUpdate = false;

                    // Tree update required if EventViewerConfig-sourcename does not match TreeView-sourcename
                    if (intsources < treeDisplay.Nodes[0].Nodes[intlogs].Nodes.Count) // only compare if in array range
                    {
                        if (treeDisplay.Nodes[0].Nodes[intlogs].Nodes[intsources].Text != eventData.eventLogs[intlogs].sources[intsources].sourceName)
                        { needSourceUpdate = true; }
                    }

                    // Tree update required if more EventViewerConfig-sources than TreeView-sources
                    if (intsources >= treeDisplay.Nodes[0].Nodes[intlogs].Nodes.Count)
                    { needSourceUpdate = true; }

                    /* ================================================================================= */



                    /* =================== Edit TreeView (Sources) =================== */

                    // Inserts EventViewerConfig-source into TreeView
                    if (needSourceUpdate == true)
                    {
                        TreeNode tempsourcenode = new TreeNode(eventData.eventLogs[intlogs].sources[intsources].sourceName);

                        // Set Source Icon
                        tempsourcenode.ImageIndex = 3;
                        tempsourcenode.SelectedImageIndex = 3;

                        // if # sources: eventViewerConfig < TreeView, perform delete on TreeView at index-intsources 
                        if (eventData.eventLogs[intlogs].sources.Count < treeDisplay.Nodes[0].Nodes[intlogs].Nodes.Count)
                        {
                            treeDisplay.Nodes[0].Nodes[intlogs].Nodes[intsources].Remove(); // Removes the non-match source-node in TreeView
                        }

                        // if # sources: eventViewerConfig = TreeView, perform replace on TreeView at index-intsources
                        else if (eventData.eventLogs[intlogs].sources.Count == treeDisplay.Nodes[0].Nodes[intlogs].Nodes.Count)
                        {
                            treeDisplay.Nodes[0].Nodes[intlogs].Nodes[intsources].Remove(); // Removes the non-match source-node in TreeView
                            treeDisplay.Nodes[0].Nodes[intlogs].Nodes.Insert(intsources, tempsourcenode); // Add eventViewerConfig source to TreeView
                        }

                        // if # sources: eventViewerConfig > TreeView, perform insert on TreeView at index-intsources
                        else if (eventData.eventLogs[intlogs].sources.Count > treeDisplay.Nodes[0].Nodes[intlogs].Nodes.Count)
                        {
                            treeDisplay.Nodes[0].Nodes[intlogs].Nodes.Insert(intsources, tempsourcenode); // Add eventViewerConfig source to TreeView
                        }

                    }

                    /* ============================================================== */


                    // if there was change to TreeView-source itself, check the current source-index again in next loop-iteration
                    if (needSourceUpdate == true)
                    { intsources--; }


                } // end source for-loop


                /* =========================== Delete Extraneous TreeView-Sources ================================= */

                // While more source-nodes in Treeview than eventViewerConfig, deletes TreeView-source-node outside of eventViewerConfig range
                while (treeDisplay.Nodes[0].Nodes[intlogs].Nodes.Count > eventData.eventLogs[intlogs].sources.Count)
                { treeDisplay.Nodes[0].Nodes[intlogs].Nodes[eventData.eventLogs[intlogs].sources.Count].Remove(); }

                /* ================================================================================================ */


                // if there was change to TreeView-log itself, check the current log-index again in next loop-iteration
                if (needLogUpdate == true)
                { intlogs--; }


            } // end log for-loop


            /* =========================== Delete Extraneous TreeView-Logs ================================= */

            // While more log-nodes in Treeview than eventViewerConfig, deletes TreeView-log-node outside of eventViewerConfig range
            while (treeDisplay.Nodes[0].Nodes.Count > eventData.eventLogs.Count)
            { treeDisplay.Nodes[0].Nodes[eventData.eventLogs.Count].Remove(); }

            /* ============================================================================================= */


        } // end function

		#endregion Treeview

        

    }
}
