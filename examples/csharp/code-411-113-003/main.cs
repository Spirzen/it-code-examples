using Microsoft.Web.WebView2.Core;
using Microsoft.Web.WebView2.WinForms;

public partial class MainForm : Form
{
    private WebView2 webView;

    public MainForm()
    {
        InitializeComponent();
        InitializeWebView();
    }

    private async void InitializeWebView()
    {
        webView = new WebView2
        {
            Dock = DockStyle.Fill
        };
        Controls.Add(webView);

        var environment = await CoreWebView2Environment.CreateAsync();
        await webView.EnsureCoreWebView2Async(environment);

        webView.CoreWebView2.WebMessageReceived += OnWebMessage;
        webView.CoreWebView2.AddWebResourceRequestedFilter(
            "https://api.example.com/*",
            CoreWebView2WebResourceContext.All
        );

        webView.CoreWebView2.Navigate("https://example.com");
    }

    private void OnWebMessage(object sender, CoreWebView2WebMessageReceivedEventArgs e)
    {
        var json = e.WebMessageAsJson;
        ProcessMessage(json);
    }
}
