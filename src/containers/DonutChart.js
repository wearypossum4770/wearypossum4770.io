import {Doughnut} from 'react-chartjs-2'

const DonutChart = props => {
    return <></>
}
export default DonutChart
//~ data: (PropTypes.object | PropTypes.func).isRequired,
//~ width: PropTypes.number,
//~ height: PropTypes.number,
//~ id: PropTypes.string,
//~ legend: PropTypes.object,
//~ options: PropTypes.object,
//~ redraw: PropTypes.bool,
//~ getDatasetAtEvent: PropTypes.func,
//~ getElementAtEvent: PropTypes.func,
//~ getElementsAtEvent: PropTypes.func
//~ // alias for getElementsAtEvent (backward compatibility)
//~ onElementsClick: PropTypes.func,

export class DonutChartClass extends React.Component {
    constructor(props) {
        super(props)
        this.chartReference = React.createRef()
    }

    componentDidMount() {
        console.log(this.chartReference) // returns a Chart.js instance reference
    }

    render() {
        const data = canvas => {
            const ctx = canvas.getContext('2d')
            const gradient = ctx.createLinearGradient(0, 0, 100, 0)
            return (backgroundColor: gradient)
        }

        return (
            <Doughnut ref={this.chartReference} data={data} options={options} />
        )
    }
}
