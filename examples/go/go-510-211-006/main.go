package parse

import (
	"reflect"
	"testing"
)

func TestExtractByTag(t *testing.T) {
	tests := []struct {
		name    string
		html    string
		tag     string
		want    []string
		wantErr bool
	}{
		{
			name: "один h1",
			html: "<html><body><h1>Hello</h1></body></html>",
			tag:  "h1",
			want: []string{"Hello"},
		},
		{
			name: "вложенный текст в a",
			html: `<a href="/x">Link <b>bold</b></a>`,
			tag:  "a",
			want: []string{"Link bold"},
		},
		{
			name: "пустой тег",
			html: "<h1>x</h1>",
			tag:  "  ",
			wantErr: true,
		},
		{
			name: "тег не найден",
			html: "<p>text</p>",
			tag:  "h1",
			want: nil,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := ExtractByTag(tt.html, tt.tag)
			if (err != nil) != tt.wantErr {
				t.Fatalf("ExtractByTag() error = %v, wantErr %v", err, tt.wantErr)
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("ExtractByTag() = %v, want %v", got, tt.want)
			}
		})
	}
}
