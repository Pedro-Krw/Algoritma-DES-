package com.pacepdro.algoritmades

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.pacepdro.algoritmades.ui.theme.AlgoritmaDESTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            AlgoritmaDESTheme {
                Scaffold(modifier = Modifier.fillMaxSize()) { innerPadding ->
                    Greeting(
                        name = "Android",
                        modifier = Modifier.padding(innerPadding)
                    )
                }
            }
        }
    }
}

@Composable
fun DESApp() {
    var inputText by remember { mutableStateOf("") }
    var keyText by remember { mutableStateOf("") }
    var resultText by remember { mutableStateOf("") }

    Column(
        modifier = Modifier.fillMaxSize().padding(16.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        TextField(
            value = inputText,
            onValueChange = { inputText = it },
            label = { Text("Input Text") }
        )
        Spacer(modifier = Modifier.height(16.dp))
        TextField(
            value = keyText,
            onValueChange = { keyText = it },
            label = { Text("Encryption Key") }
        )
        Spacer(modifier = Modifier.height(16.dp))
        Row {
            Button(onClick = {
                // Panggil fungsi enkripsi (nantinya akan menggunakan Python)
            }) {
                Text("Encrypt")
            }
            Spacer(modifier = Modifier.width(16.dp))
            Button(onClick = {
                // Panggil fungsi dekripsi (nantinya akan menggunakan Python)
            }) {
                Text("Decrypt")
            }
        }
        Spacer(modifier = Modifier.height(16.dp))
        Text(text = "Result: $resultText")
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    AlgoritmaDESTheme {
        Greeting("Android")
    }
}