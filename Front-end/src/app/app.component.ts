import { Component } from '@angular/core';
import { FlowerService } from './services/flower.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})


export class AppComponent {

  flowerCode: string;
  constructor(private flowerService: FlowerService) {
    console.log(this.flowerCode)
  }

  floweData = {
    "crocus_sativus.jpg": [5.1, 3.5, 1.4, 0.3],
    "dietes_bicolor.jpg": [4.7, 3.2, 1.6, 0.2],
    "dietes_grandiflora.jpg": [4.9, 3, 1.4, 0.2],
    "eleutherine_bulbosa.jpg": [5, 3.6, 1.4, 0.2],
    "freesia_spp.jpg": [4.6, 3.4, 1.4, 0.3],
    "gladiolus_natalensis.jpg": [4.4, 2.9, 1.4, 0.2],
    "iris_clarkei.jpg": [5.4, 3.7, 1.5, 0.2],
    "iris_crocea.jpg": [5.8, 4, 1.2, 0.2],
    "iris_domestica.jpg": [5.7, 4.4, 1.5, 0.4],
    "iris_hookeriana": [4.9, 3.1, 1.5, 0.1],
    "iris_japonica": [5.4, 3.4, 1.5, 0.4]
  }

  outputData = [
    {
      name: "Crocus Sativus",
      id: 1,
      poisnous: "No",
      impact: "Helps to maintain Good health",
      edible: "Yes",
      medicinal_value: ["Used as an ingredient in cure for kidney problems", "Used to reduce headache and hangover"],
      use: "It is Used in Herbal Medicines"
    },
    {
      name: "Dietes Bicolor",
      id: 2,
      poisnous: "No",
      impact: "No",
      edible: "Yes	Roots are used in african medicine",
      medicinal_value: ["Used as an ingredient in cure for kidney problems", "Used to reduce headache and hangover"],
      use: "Protect from Dehydration"
    },

    {
      name: "Dietes Grandiflora",
      id: 3,
      poisnous: "Yes",
      impact: "Causes rashes or skin problems",
      edible: "No",
      medicinal_value: ["Currently No Medicinal Value"],
      use: "No"
    }
    ,
    {
      name: "Eleutherine bulbosa",
      id: 4,
      poisnous: "No",
      impact: "No",
      edible: "Yes",
      medicinal_value: ["Ingested to kill Intestinal parasites", "treatment for diarrhoea, Haemorrhagia and open wounds"],
      use: "It  is an important element of the American Indian pharmacopeia"
    },
    {
      name: "Freesia spp.",
      id: 5,
      poisnous: "No",
      impact: "No",
      edible: "Yes",
      medicinal_value: ["Currently No Medicinal Value"],
      use: "They grown as ornamental plants in gardens or are sold as cut flowers"
    },
    {
      name : "Gladiolus natalensis",
      id : 6,
      poisnous : "Yes",
      impact : "eaten uncooked may cause some physiological issues",
      edible : "No",
      medicinal_value : ["Cure both constipation and severe dysentery"],
      use : "No",
      remedy : "dietes_bicolor.jpg"
    },
    {
      name : "Iris clarkei",
      id : 7,
      poisnous : "Yes",
      impact : "Controls heart Rate",
      edible : "No",
      medicinal_value : ["Used in Chinese medicine"],
      use : "It is used to identify hybrids and classification of groupings"
    }
  ]


  title = 'flowerProject';
  url: string = "../assets/lily.jpg";
  imageName: string;
  onFileChanged(event) {
    const file = event.target.files[0];
    this.imageName = file.name;
    this.url = `../assets/${file.name}`;
  }

  detectInformation() {

    let output = this.floweData[this.imageName];
    this.flowerService.getFlowerCode(output).subscribe((result) => {
      this.flowerCode = result.payload.flower_code;
    })
  }

  display() {
    for(let i=0; i<this.outputData.length; i++)
    {
      if(this.outputData[i].id == parseInt(this.flowerCode))
      { 
        this.url = `../assets/${this.outputData[i].remedy}`;
        this.imageName = this.outputData[i].remedy;
        break;
      }
    }

    this.detectInformation();
  }
}
