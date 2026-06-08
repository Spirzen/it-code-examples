configuration WebServerConfig {
    Import-DscResource -ModuleName PSDesiredStateConfiguration
    
    Node "WebServer01" {
        WindowsFeature WebServer {
            Ensure = "Present"
            Name = "Web-Server"
        }
        
        File WebContent {
            Ensure = "Present"
            DestinationPath = "C:\inetpub\wwwroot"
            Type = "Directory"
        }
        
        Service W3Svc {
            Name = "W3SVC"
            State = "Running"
            StartupType = "Automatic"
        }
    }
}
