var insertCmd = &cobra.Command{
    Use:   "insert [name] [phone]",
    Short: "Добавить контакт",
    Args:  cobra.ExactArgs(2),
    RunE: func(cmd *cobra.Command, args []string) error {
        name, phone := args[0], args[1]
        return store.Insert(name, phone)
    },
}

func init() {
    rootCmd.AddCommand(insertCmd)
    insertCmd.Flags().StringVarP(&configPath, "config", "c", "phonebook.yaml", "путь к конфигу")
}
