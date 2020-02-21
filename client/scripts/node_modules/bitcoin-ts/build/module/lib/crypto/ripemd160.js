import { instantiateRustWasm, ripemd160Base64Bytes } from '../bin/bin';
import { base64ToBin } from '../utils/utils';
/**
 * The most performant way to instantiate ripemd160 functionality. To avoid
 * using Node.js or DOM-specific APIs, you can use `instantiateRipemd160`.
 *
 * @param webassemblyBytes A buffer containing the ripemd160 binary.
 */
export const instantiateRipemd160Bytes = async (webassemblyBytes) => {
    const wasm = await instantiateRustWasm(webassemblyBytes, './ripemd160', 'ripemd160', 'ripemd160_init', 'ripemd160_update', 'ripemd160_final');
    return {
        final: wasm.final,
        hash: wasm.hash,
        init: wasm.init,
        update: wasm.update
    };
};
export const getEmbeddedRipemd160Binary = () => base64ToBin(ripemd160Base64Bytes).buffer;
/**
 * An ultimately-portable (but slower) version of `instantiateRipemd160Bytes`
 * which does not require the consumer to provide the ripemd160 binary buffer.
 */
export const instantiateRipemd160 = async () => instantiateRipemd160Bytes(getEmbeddedRipemd160Binary());
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicmlwZW1kMTYwLmpzIiwic291cmNlUm9vdCI6IiIsInNvdXJjZXMiOlsiLi4vLi4vLi4vLi4vc3JjL2xpYi9jcnlwdG8vcmlwZW1kMTYwLnRzIl0sIm5hbWVzIjpbXSwibWFwcGluZ3MiOiJBQUFBLE9BQU8sRUFFTCxtQkFBbUIsRUFDbkIsb0JBQW9CLEVBQ3JCLE1BQU0sWUFBWSxDQUFDO0FBQ3BCLE9BQU8sRUFBRSxXQUFXLEVBQUUsTUFBTSxnQkFBZ0IsQ0FBQztBQXFEN0M7Ozs7O0dBS0c7QUFDSCxNQUFNLENBQUMsTUFBTSx5QkFBeUIsR0FBRyxLQUFLLEVBQzVDLGdCQUE2QixFQUNULEVBQUU7SUFDdEIsTUFBTSxJQUFJLEdBQUcsTUFBTSxtQkFBbUIsQ0FDcEMsZ0JBQWdCLEVBQ2hCLGFBQWEsRUFDYixXQUFXLEVBQ1gsZ0JBQWdCLEVBQ2hCLGtCQUFrQixFQUNsQixpQkFBaUIsQ0FDbEIsQ0FBQztJQUNGLE9BQU87UUFDTCxLQUFLLEVBQUUsSUFBSSxDQUFDLEtBQUs7UUFDakIsSUFBSSxFQUFFLElBQUksQ0FBQyxJQUFJO1FBQ2YsSUFBSSxFQUFFLElBQUksQ0FBQyxJQUFJO1FBQ2YsTUFBTSxFQUFFLElBQUksQ0FBQyxNQUFNO0tBQ3BCLENBQUM7QUFDSixDQUFDLENBQUM7QUFFRixNQUFNLENBQUMsTUFBTSwwQkFBMEIsR0FBRyxHQUFHLEVBQUUsQ0FDN0MsV0FBVyxDQUFDLG9CQUFvQixDQUFDLENBQUMsTUFBTSxDQUFDO0FBRTNDOzs7R0FHRztBQUNILE1BQU0sQ0FBQyxNQUFNLG9CQUFvQixHQUFHLEtBQUssSUFBd0IsRUFBRSxDQUNqRSx5QkFBeUIsQ0FBQywwQkFBMEIsRUFBRSxDQUFDLENBQUMifQ==